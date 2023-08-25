from django.urls import path
from .views import hw

urlpatterns = [
    path('lesson_4/', hw)
]