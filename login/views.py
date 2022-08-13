from django.shortcuts import render
from .models import CloudUser
# Create your views here.

# def CloudUser_list(request):  #예전에 연습한다고 만들어놓은 model의 view임. 신경 끌 것.
#     qs = CloudUser.objects.all()
#     return render(request, 'login/CloudUser_list.html', {
#         'CloudUser_list': qs,
#     })