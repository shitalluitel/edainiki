from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from apps.common.constants.commons import TEMPLATE_FOR, CHARKILLA
from apps.setting.constants import TEMPLATE_TYPE


class Setting(models.Model):
    pass


class LetterTemplate(models.Model):
    model = models.CharField(max_length=120, choices=TEMPLATE_FOR, default=CHARKILLA)
    # template = models.TextField(max_length=10000)
    template = RichTextUploadingField()
    type = models.CharField(max_length=8, choices=TEMPLATE_TYPE, null=True)

    def __str__(self):
        return f'{self.model} - {self.type}'
