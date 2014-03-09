from django.contrib import admin
from charity_app.models import Charity, Video


class CharityAdmin(admin.ModelAdmin):
    list_display = ("name", "posted", "user")
    search_fields = ("name",)
    readonly_fields = ("user",)


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "posted", "charity")
    search_fields = ("title",)
    readonly_fields = ("charity",)


admin.site.register(Charity, CharityAdmin)
admin.site.register(Video, VideoAdmin)