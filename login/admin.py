from django.contrib import admin
from .models import CloudUser

# Register your models here.
#admin.site.register(CloudUser)

@admin.register(CloudUser)
class CloudUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_pw', 'user_name', 'user_email', 'user_birthdate']
