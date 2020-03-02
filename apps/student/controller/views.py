from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView

from apps.student.controller.forms import (StudentCreateForm, StudentUpdateForm, StudentLetterForm)
from apps.student.models import Student, StudentLetter


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


class StudentLetterView(CreateView):
    success_url = reverse_lazy('student:list')
    form_class = StudentLetterForm
    template_name = 'student/letter.html'


class StudentLetterUpdateView(UpdateView):
    success_url = reverse_lazy('student:list')
    form_class = StudentLetterForm
    template_name = 'student/letter.html'
    queryset = StudentLetter.objects.all()


class StudentLetterDetailView(DetailView):
    template_name = 'student/letter_detail.html'
    queryset = StudentLetter.objects.all()
