from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'file', 'get_html_photo', 'time_create', 'time_update', 'course')
    list_display_links = ('id', 'title')
    list_filter = ('time_create', )
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=175>")

    get_html_photo.short_description = 'Миниатюра'


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'type_course', 'time_create', 'time_update')
    list_display_links = ('id', 'title')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=175>")

    get_html_photo.short_description = 'Миниатюра'


admin.site.register(Posts, PostsAdmin)
admin.site.register(Courses, CoursesAdmin)
