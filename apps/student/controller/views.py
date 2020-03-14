from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from apps.student.controller.forms import (StudentCreateForm, StudentUpdateForm, StudentLetterForm)
from apps.student.models import Student, StudentLetter
from apps.student.utils import generate_letter


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

    def get_context_data(self, **kwargs):
        # kwargs['placeholders'] = {
        #     x.attname: '{{ _ }}'.replace('_', x.attname) for x in Student._meta.fields if
        #     x not in ['id', 'created_at', 'modified_at']
        # }
        #
        kwargs['placeholders'] = list(
            map(
                lambda x: '{{ _ }}'.replace('_', x.attname),
                Student._meta.fields
            )
        )

        return super().get_context_data(**kwargs)


class StudentLetterUpdateView(UpdateView):
    success_url = reverse_lazy('student:list')
    form_class = StudentLetterForm
    template_name = 'student/letter.html'
    queryset = StudentLetter.objects.all()


class StudentLetterDetailView(DetailView):
    template_name = 'student/letter_detail.html'
    queryset = StudentLetter.objects.all()

    def get_context_data(self, **kwargs):
        student = Student.objects.filter(
            id=self.kwargs.get('student_id')
        ).first()

        letter = StudentLetter.objects.filter(id=self.kwargs.get('pk')).first()
        kwargs['template'] = generate_letter(
            instance=student,
            letter_template=letter.template
        )
        return super().get_context_data(**kwargs)



