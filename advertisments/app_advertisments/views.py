from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import AdvertisementForm
# Create your views here.
from .models import Advertisments

def index(request):
    advertisements = Advertisments.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_adv = form.save(commit = False)
            new_adv.user = request.user
            new_adv.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)