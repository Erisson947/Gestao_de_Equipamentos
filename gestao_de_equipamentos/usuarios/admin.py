from django.contrib import admin

from usuarios import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass

