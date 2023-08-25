from django.shortcuts import render
from django.http import HttpResponse

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
    form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)