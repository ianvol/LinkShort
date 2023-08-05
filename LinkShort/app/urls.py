
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views  # Import views from the 'app' directory

urlpatterns = [
    path("", views.index, name="home"),
    path('my-links/', views.my_links, name='my_links'),
    ##path('<str:short_url>/', views.redirect_to_long_url, name='redirect_to_long_url'),
    ##path("<int:uuid>/", views.detail, name="detail"),
    ##path("<str:redirect_to_long_url>/", views.redirect_to_long_url, name="redirect_to_long_url_by_name"),
    path("admin/", admin.site.urls),
]