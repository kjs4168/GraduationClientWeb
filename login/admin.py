from django.contrib import admin
from .models import CloudUser

# Register your models here.
#admin.site.register(CloudUser)

@admin.register(CloudUser)
class CloudUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_date', 'email', 'created_at', 'updated_at']
