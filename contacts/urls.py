# contacts/urls.py

from django.urls import path
from .views import contact_view, success_view

urlpatterns = [
    # URL for the contact form page
    path('contact/', contact_view, name='contact'),
    # URL for the success/thank you page
    path('success/', success_view, name='success'),
]