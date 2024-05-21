from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from writers.models import Writer


class VblogUserAdmin(UserAdmin):
    pass


admin.site.register(Writer, VblogUserAdmin)
