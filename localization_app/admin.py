from django.contrib import admin
from .models import *


class LocalizedStringInline(admin.TabularInline):
    model = LocalizedString


class DataStringAdmin(admin.ModelAdmin):
    inlines = [
        LocalizedStringInline,
    ]


admin.site.register(Language)
admin.site.register(DataString, DataStringAdmin)
admin.site.register(LocalizedString)
