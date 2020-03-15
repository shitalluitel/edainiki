from django import forms
from django.forms import formset_factory

from apps.charkilla.models import Charkilla, CharkillaDetail


# Create your form here.


class CharkillaCreateForm(forms.ModelForm):
    class Meta:
        model = Charkilla
        fields = "applicant_name", "eng_date", "nep_date"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })


class CharkillaUpdateForm(forms.ModelForm):
    class Meta:
        model = Charkilla
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })


class CharkillaDetailForm(forms.ModelForm):
    class Meta:
        model = CharkillaDetail
        fields = [
            'kitta_no', 'map_sheet_no', 'total_area', 'east_piller',
            'west_piller', 'north_piller', 'south_piller', 'description'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })


CharkillaDetailFormSet = formset_factory(CharkillaDetailForm)
