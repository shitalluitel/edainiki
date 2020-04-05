from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
# from django_summernote.widgets import SummernoteWidget

from apps.setting.models import Setting, LetterTemplate


# Create your form here.


class SettingCreateForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = "__all__"


class SettingUpdateForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = "__all__"


class LetterTemplateForm(forms.ModelForm):
    # template = forms.CharField(widget=SummernoteWidget())
    template = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = LetterTemplate
        fields = 'template',


class TemplateRedirectForm(forms.ModelForm):
    class Meta:
        model = LetterTemplate
        fields = 'model', 'type',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    'class': 'form-control'
                }
            )