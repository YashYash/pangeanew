from django.contrib import admin

# Register your models here.
from user_app.models import ActiveUser, Newsfeed


class ActiveUserAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    # readonly_fields = ("user",)


class NewsfeedAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    # readonly_fields = ("user",)

admin.site.register(ActiveUser, ActiveUserAdmin)
admin.site.register(Newsfeed, NewsfeedAdmin)