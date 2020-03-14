from django.urls import path

from apps.student.controller.views import (StudentListView, StudentCreateView,
                                           StudentEditView, StudentDetailView, StudentDeleteView,
                                           StudentLetterView, StudentLetterDetailView, StudentLetterUpdateView)

app_name = 'student'

urlpatterns = [
    path('', StudentListView.as_view(), name="list"),
    path('create/', StudentCreateView.as_view(), name="create"),
    path('update/<int:pk>', StudentEditView.as_view(), name="update"),
    path('detail/<int:pk>', StudentDetailView.as_view(), name="detail"),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name="delete"),
    path('letter/', StudentLetterView.as_view(), name="letter"),
    path('letter/<int:pk>', StudentLetterUpdateView.as_view(), name="letter-update"),
    path('letter/detail/<int:pk>/student/<int:student_id>', StudentLetterDetailView.as_view(), name="letter-detail"),
]
