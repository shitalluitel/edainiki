from django.contrib import admin

# Register your models here.
from apps.setting.models import Setting, LetterTemplate

admin.site.register(Setting)
admin.site.register(LetterTemplate)