from django.shortcuts import render
from .models import CloudUser
# Create your views here.

def CloudUser_list(request):
    qs = CloudUser.objects.all()
    return render(request, 'login/CloudUser_list.html', {
        'CloudUser_list': qs,
    })