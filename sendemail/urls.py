from django.urls import path

from .views import listing_view

urlpatterns = [
    path('listing/', listing_view, name='listing'),
]
