import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.common.constants.commons import FILE_TYPES, CITIZENSHIP
from apps.common.utils.commons import unique_slugify


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at', '-modified_at')


class SlugModel(models.Model):
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    class Meta:
        abstract = True

    def _get_slug_text(self):
        assert any([hasattr(self, 'name'), hasattr(self, 'title')])
        slug_text = ''
        if hasattr(self, 'name'):
            slug_text = self.name.lower()
        elif hasattr(self, 'title'):
            slug_text = self.title.lower()
        return slug_text

    def _get_previous_slug_text(self):
        if self.id:
            _pre_data = self.__class__.objects.get(id=self.id)
            return _pre_data._get_slug_text()
        return None

    def save(self, *args, **kwargs):
        slug_text = self._get_slug_text()
        pre_slug_text = self._get_previous_slug_text()
        if not self.slug or slug_text != pre_slug_text:
            unique_slugify(self, slug_text)
        return super().save(*args, **kwargs)


class DainikiModel(models.Model):
    applicant_name = models.CharField(
        max_length=150,
        error_messages={'max_length': 'कृपया नामाको लम्बाई ६४ भन्दा कम राख्नुहोस।'}
    )
    eng_date = models.DateField(null=True)
    nep_date = models.CharField(
        max_length=10,
        error_messages={'max_length': 'तपाईले छान्नु भएको मिति मिलेको छैन। कृपया सहि मिति छनोट गर्नुहोस्।'},
        null=True
    )
    is_deleted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    form_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.applicant_name


class DainikiDocumentModel(models.Model):
    content_type = models.ForeignKey(ContentType, related_name='documents', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    document = models.FileField(
        upload_to='',
        validators=[
            FileExtensionValidator(['pdf', 'jpeg', 'jpg', 'png', 'doc', 'docx'])
        ]
    )
    type = models.CharField(max_length=20, choices=FILE_TYPES, default=CITIZENSHIP)

    class Meta:
        abstract = True


class BaseModel(TimeStampModel, DainikiModel):
    class Meta:
        abstract = True
