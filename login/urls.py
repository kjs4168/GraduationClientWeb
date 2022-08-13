from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login/loginForm.html'), name='login'),
    path('register/', include('register.urls')),
]