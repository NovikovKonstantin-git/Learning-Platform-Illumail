from django.contrib import admin
from .models import Courses, Posts, CompletedTaskModel, Category, Comments


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'time_created', 'time_updated')
    list_filter = ('title', 'category', 'time_created')
    search_fields = ('title', )


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'post_type', 'time_created', 'time_updated')
    list_filter = ('title', 'time_created', 'course')
    search_fields = ('title',)


class ComplitedTaskModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'post', 'time_load')
    list_filter = ('user', 'time_load')
    search_fields = ('user', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(CompletedTaskModel, ComplitedTaskModelAdmin)
admin.site.register(Comments)