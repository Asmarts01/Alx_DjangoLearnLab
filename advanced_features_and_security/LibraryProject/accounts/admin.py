from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth')
    search_fields = ('username', 'email')