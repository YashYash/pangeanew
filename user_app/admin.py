from django.contrib import admin

# Register your models here.
from user_app.models import ActiveUser


class ActiveUserAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    # readonly_fields = ("user",)


admin.site.register(ActiveUser, ActiveUserAdmin)