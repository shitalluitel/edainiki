from django import forms
from apps.settings.models import Settings
# Create your form here.


class SettingsCreateForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = "__all__"


class SettingsUpdateForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = "__all__"

