"""
Definition of urls for LinkShort.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')),  # Include the URLs from 'app/urls.py'
    path("admin/", admin.site.urls),
]



