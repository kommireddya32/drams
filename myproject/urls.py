from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login/')),  # 👈 Redirect root path to login
    path('', include('accounts.urls')),
]
