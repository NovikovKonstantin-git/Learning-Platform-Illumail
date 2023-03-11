from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'patronymic', 'user', 'bio', 'get_html_photo', 'time_created', 'time_updated')
    list_display_links = ('first_name', 'last_name', 'patronymic')
    list_filter = ('time_created', )
    save_on_top = True

    def get_html_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=85>")

    get_html_photo.short_description = 'Миниатюра'


admin.site.register(Profile, ProfileAdmin)

