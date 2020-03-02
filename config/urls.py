from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from apps.common.views import HomePageView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('setting/', include('apps.setting.controller.urls', namespace='settings')),
                  path('student/', include('apps.student.controller.urls', namespace='students')),
                  path('', HomePageView.as_view(), name="home"),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
