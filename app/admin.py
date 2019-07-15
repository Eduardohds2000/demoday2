from django.contrib import admin
from .models import Login

# Register your models here.

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display =['id','nome']
