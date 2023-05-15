from django.contrib import admin
from .models import StudyGroup, PostsInStudyGroup, CompletedTaskInStudyGroup


class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'time_created', 'time_updated')
    list_filter = ('title', 'time_created')
    search_fields = ('title', )


class PostsInStudyGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'study_group', 'post_type', 'time_created', 'time_updated')
    list_filter = ('title', 'time_created', 'study_group')
    search_fields = ('title',)


class ComplitedTaskInStudyGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'post', 'time_load')
    list_filter = ('user', 'time_load')
    search_fields = ('user', )


admin.site.register(StudyGroup, StudyGroupAdmin)
admin.site.register(PostsInStudyGroup, PostsInStudyGroupAdmin)
admin.site.register(CompletedTaskInStudyGroup, ComplitedTaskInStudyGroupAdmin)
