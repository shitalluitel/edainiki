from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.core.validators import EmailValidator, URLValidator
from django.db import models

# Create your models here.
from apps.common.constants.commons import TEMPLATE_FOR, CHARKILLA
from apps.common.models.common import BaseModel, TimeStampModel
from apps.common.validators.commons import ward_validation
from apps.setting.constants import TEMPLATE_TYPE, WARD, OFFICE_TYPE, ORGANIZATION_TYPE, RURAl_MUNICIPALITY


class Setting(TimeStampModel):
    office_type = models.CharField(max_length=9, choices=OFFICE_TYPE, default=WARD)
    organization_type = models.CharField(max_length=18, choices=ORGANIZATION_TYPE, default=RURAl_MUNICIPALITY)

    organization_name_np = models.CharField(max_length=552)
    organization_name_en = models.CharField(max_length=225)

    country_np = models.CharField(max_length=225)
    country_en = models.CharField(max_length=124)

    province_np = models.CharField(max_length=225)
    province_en = models.CharField(max_length=124)

    district_np = models.CharField(max_length=225)
    district_en = models.CharField(max_length=124)

    address_np = models.CharField(max_length=225)
    address_en = models.CharField(max_length=124)

    ward_no_np = models.CharField(max_length=8, validators=[ward_validation])
    ward_no_en = models.CharField(max_length=2, validators=[ward_validation])

    section_np = models.CharField(max_length=225)

    email = models.EmailField()
    website = models.CharField(max_length=2048, validators=[URLValidator])
    phone_no = models.CharField(max_length=20)
    footer_slogan = models.CharField(max_length=225)
    office_slogan_np = models.CharField(max_length=225)
    office_slogan_en = models.CharField(max_length=225)

    def __str__(self):
        return self.organization_name_en


class FiscalYear(TimeStampModel):
    name_np = models.CharField(max_length=14, validators=[])
    name_en = models.CharField(max_length=14, validators=[])
    applicable_from = models.DateField()
    applicable_to = models.DateField()

    def __str__(self):
        return self.name_en


class LetterTemplate(models.Model):
    model = models.CharField(max_length=120, choices=TEMPLATE_FOR, default=CHARKILLA)
    # template = models.TextField(max_length=10000)
    template = RichTextUploadingField()
    type = models.CharField(max_length=8, choices=TEMPLATE_TYPE, null=True)

    def __str__(self):
        return f'{self.model} - {self.type}'
