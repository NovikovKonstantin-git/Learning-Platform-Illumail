from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("chat/", include('chat.urls')),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', include('users.urls')),
    path('', include('courses.urls')),
    path('', include('study_groups.urls')),
    path('', include('payments.urls')),
    path('', include('forum.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
