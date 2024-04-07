from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from myauth.models import VblogUser


class VblogUserAdmin(UserAdmin):
    pass


admin.site.register(VblogUser, VblogUserAdmin)
