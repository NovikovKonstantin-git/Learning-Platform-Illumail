from django.contrib import admin
from .models import *


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'type_course', 'price', 'time_created', 'time_updated')
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


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'author', 'course', 'time_created')
    list_filter = ('author', 'time_created', 'course')
    search_fields = ('comment_text', )


class QuizAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'question', 'true_answer')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'user_answer')


"""Новое"""


class GoodTestAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'test')


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(CompletedTaskModel, ComplitedTaskModelAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Progress)

# admin.site.register(GoodTestModel, GoodTestAdmin)
# admin.site.register(QuestionModel, QuestionAdmin)
# admin.site.register(AnswerModel)