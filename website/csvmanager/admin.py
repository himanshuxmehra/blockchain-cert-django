from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import *


# Custom Class
class UserAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'name', 'university_name', 'date_joined', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name', 'university_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('User Details', {'fields': ('name', 'university_name', 'date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active')}
         ),
        ('User Details', {'fields': ('name', 'university_name')}),
    )


class CSVFileAdmin(admin.ModelAdmin):
    readonly_fields = ('result_csv',)


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(CSVFile, CSVFileAdmin)
