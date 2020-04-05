from django import forms
# from django_summernote.widgets import SummernoteWidget

from apps.student.models import Student
from django import forms

from apps.student.models import Student


# from django_summernote.widgets import SummernoteWidget


# Create your form here.


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })
