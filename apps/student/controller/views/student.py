from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from apps.student.controller.forms import (StudentCreateForm, StudentUpdateForm)
from apps.student.models import Student


class StudentCreateView(CreateView):
    queryset = Student.objects.all()
    form_class = StudentCreateForm
    template_name = 'student/create.html'
    success_url = reverse_lazy('student:list')


class StudentListView(ListView):
    queryset = Student.objects.all()
    template_name = 'student/list.html'


class StudentEditView(UpdateView):
    queryset = Student.objects.all()
    form_class = StudentUpdateForm
    template_name = 'student/create.html'
    success_url = reverse_lazy('student:list')


class StudentDetailView(DetailView):
    queryset = Student.objects.all()
    template_name = 'student/list.html'


class StudentDeleteView(DeleteView):
    queryset = Student.objects.all()
    template_name = 'student/create.html'
    success_url = reverse_lazy('student:list')
