from django.contrib import admin
from giver_app.models import Giver


class GiverAdmin(admin.ModelAdmin):
    list_display = ("name", "charities")
    search_fields = ("name",)
    readonly_fields = ("user",)


admin.site.register(Giver, GiverAdmin)
