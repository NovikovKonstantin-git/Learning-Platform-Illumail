from django.contrib import admin
from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'patronymic', 'email', 'photo', 'bio', 'time_created',
                    'time_updated', 'users_courses')
    list_filter = ('time_created', )
    search_fields = ('username', 'first_name', 'last_name', 'patronymic', 'email')
    save_on_top = True


admin.site.register(CustomUser, CustomUserAdmin)
