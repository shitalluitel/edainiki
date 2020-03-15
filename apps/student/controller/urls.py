from django.urls import path

from apps.student.controller.views.student import (
    StudentListView, StudentCreateView,
    StudentEditView, StudentDetailView, StudentDeleteView
)

app_name = 'student'

urlpatterns = [
    path('', StudentListView.as_view(), name="list"),
    path('create/', StudentCreateView.as_view(), name="create"),
    path('update/<int:pk>', StudentEditView.as_view(), name="update"),
    path('detail/<int:pk>', StudentDetailView.as_view(), name="detail"),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name="delete"),
]
