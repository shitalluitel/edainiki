from django.urls import path, re_path

from apps.charkilla.controller.views import (
    CharkillaListView, CharkillaCreateView, CharkillaDeleteView,
    CharkillaEditView, CharkillaDetailView, CharkillaTemplateView
)

app_name = 'charkilla'

urlpatterns = [
    path('', CharkillaListView.as_view(), name="list"),
    path('create/', CharkillaCreateView.as_view(), name="create"),
    path('update/<int:pk>/', CharkillaEditView.as_view(), name="update"),
    path('detail/<int:pk>/', CharkillaDetailView.as_view(), name="detail"),
    path('delete/<int:pk>/', CharkillaDeleteView.as_view(), name="delete"),
    re_path(r'template/(?P<pk>\d+)/(?P<type>(nibedan|sifaris))/$', CharkillaTemplateView.as_view(), name="template"),
]
