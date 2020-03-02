from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=32)
    address = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class StudentLetter(models.Model):
    template = RichTextUploadingField()
