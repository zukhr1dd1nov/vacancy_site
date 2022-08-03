from django.contrib import admin
from .models import User, Employer

# Register your models here.

class EmployerInline(admin.TabularInline):
    model = Employer

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        EmployerInline,
    ]