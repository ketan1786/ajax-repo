from django.contrib import admin
from .models import CurdUser


class AdminDisp(admin.ModelAdmin):
    list_display = ['name', 'address', 'age']


admin.site.register(CurdUser, AdminDisp)