from django.urls import path

from apps.settings.controller.views import (SettingsListView, SettingsCreateView,
                                            SettingsEditView, SettingsDetailView, SettingsDeleteView)

app_name = 'settings'

urlpatterns = [
    path('', SettingsListView.as_view(), name="list"),
    path('create', SettingsCreateView.as_view(), name="create"),
    path('update', SettingsEditView.as_view(), name="update"),
    path('detail', SettingsDetailView.as_view(), name="detail"),
    path('delete', SettingsDeleteView.as_view(), name="delete")
]
