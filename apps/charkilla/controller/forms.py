from django import forms
from django.forms import formset_factory

from apps.charkilla.models import Charkilla, CharkillaDetail
from apps.common.utils.template_util import get_template_field_map


class CharkillaCreateForm(forms.ModelForm):
    class Meta:
        model = Charkilla
        fields = "applicant_name", "eng_date", "nep_date"

    def __init__(self, *args, **kwargs):
        self.Meta.fields = get_template_field_map('Charkilla')
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'borderless-input',
            })


class CharkillaUpdateForm(forms.ModelForm):
    class Meta:
        model = Charkilla
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control borderless-input',
            })


class CharkillaDetailForm(forms.ModelForm):
    class Meta:
        model = CharkillaDetail
        fields = [
            'kitta_no', 'map_sheet_no', 'total_area', 'east_piller',
            'west_piller', 'north_piller', 'south_piller', 'description'
        ]

    def __init__(self, *args, **kwargs):
        self.Meta.fields = get_template_field_map('Charkilla', related=True)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control borderless-input',
            })


CharkillaDetailFormSet = formset_factory(CharkillaDetailForm)
