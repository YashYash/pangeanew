from django.contrib import admin
from charity_app.models import Charity, Video, ClickCount


class CharityAdmin(admin.ModelAdmin):
    list_display = ("name", "posted", "user")
    search_fields = ("name",)


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "posted", "charity")
    search_fields = ("title",)





admin.site.register(Charity, CharityAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(ClickCount)