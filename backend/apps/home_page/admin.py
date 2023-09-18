from django.contrib import admin
from . import models


@admin.register(models.HeaderNavigation)
class HeaderNavigationAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'link',
    ]
    list_display = [
        'id',
        '__str__',
        'link',
    ]


@admin.register(models.Adventage)
class AdventageAdmin(admin.ModelAdmin):
    fields = [
        'adventage_row_1',
        'adventage_row_2',
        'adventage_row_3',
    ]
    list_display = [
        'id',
        '__str__',
    ]
