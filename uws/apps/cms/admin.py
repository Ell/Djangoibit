from django.contrib import admin

from cms.models import Show, Grouping, Page


class ShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'dj')


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'grouping')


class GroupingAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')


admin.site.register(Show, ShowAdmin)
admin.site.register(Grouping, GroupingAdmin)
admin.site.register(Page, PageAdmin)
