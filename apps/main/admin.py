from django.contrib import admin
from apps.main.models import Setting
# Register your models here.

# admin.site.register(Setting)

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'logo',)
    list_editable = ("logo",)
    list_filter = ("title", "description")
    search_fields = ("title",)
