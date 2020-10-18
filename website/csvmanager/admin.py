from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Custom Class
class UserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'name', 'university_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'name', 'university_name')
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('User Details', {'fields': ('name', 'university_name', 'date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
        ('User Details', {'fields': ('name', 'university_name')}),
    )


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(CSVFile)
