from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

app_name = 'login'

urlpatterns = [
    path('', LoginView.as_view(template_name='login/loginForm.html'), name='login'),
    path('register/', include('register.urls')),
]