from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setting/', include('apps.settings.controller.urls', namespace='settings')),
]
