from django.contrib import admin
from .models import CloudUser

# Register your models here.
#admin.site.register(CloudUser)

@admin.register(CloudUser)  #admin페이지 연습한다고 등록해놓은 model
class CloudUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_pw', 'user_name', 'user_email', 'user_birthdate']