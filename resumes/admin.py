from django.contrib import admin
from .models import Resume, User

admin.site.register(Resume)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']