from django.contrib import admin
from forum.models import ForumSection, ForumSubsection, ForumCommunication


class ForumSubsectionAdmin(admin.ModelAdmin):
    list_display = ('subsection', 'section')


class ForumCommunicationAdmin(admin.ModelAdmin):
    list_display = ('subsection', 'user', 'comm_text', 'date_text')


admin.site.register(ForumSection)
admin.site.register(ForumSubsection, ForumSubsectionAdmin)
admin.site.register(ForumCommunication, ForumCommunicationAdmin)
