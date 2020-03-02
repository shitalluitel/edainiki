from django.urls import path

from apps.setting.controller.views import (SettingListView, SettingCreateView,
                                           SettingEditView, SettingDetailView, SettingDeleteView)

app_name = 'setting'

urlpatterns = [
    path('', SettingListView.as_view(), name="list"),
    path('create/', SettingCreateView.as_view(), name="create"),
    path('update/', SettingEditView.as_view(), name="update"),
    path('detail/', SettingDetailView.as_view(), name="detail"),
    path('delete/', SettingDeleteView.as_view(), name="delete")
]
