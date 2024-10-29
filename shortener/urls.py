from django.urls import path, include

from .views import home, redirect_to_url

urlpatterns = [
    path('', home, name='home'),
    path('<str:short_url>/', redirect_to_url, name='redirect_to_url'),
]
