from django.urls import path
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),  # ✅ Redirect root URL to login
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('input/', views.input_view, name='input'),
    path('output/', views.output_view, name='output'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('report/', views.report_view, name='report'),
]
