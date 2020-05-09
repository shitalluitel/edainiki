from django.urls import path

from apps.setting.controller.views.setting import (
    SettingListView, SettingCreateView,
    SettingEditView, SettingDetailView, SettingDeleteView
)
from apps.setting.controller.views.template import (
    LetterTemplateUpdateView, TemplateRedirectView
)

app_name = 'setting'

urlpatterns = [
    path('', SettingListView.as_view(), name="list"),
    path('create/', SettingCreateView.as_view(), name="create"),
    path('update/', SettingEditView.as_view(), name="update"),
    path('detail/', SettingDetailView.as_view(), name="detail"),
    path('delete/', SettingDeleteView.as_view(), name="delete"),
    path('template/<int:pk>/', LetterTemplateUpdateView.as_view(), name="template-update"),
    path('template/', TemplateRedirectView.as_view(), name="template-create"),
]
