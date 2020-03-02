from django import forms
from apps.setting.models import Setting
# Create your form here.


class SettingCreateForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = "__all__"


class SettingUpdateForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = "__all__"

