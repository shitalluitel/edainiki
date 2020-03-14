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


class StudentSubjects(models.Model):
    student = models.ForeignKey(Student, related_name='subjects', on_delete=models.CASCADE)
    subject = models.CharField(max_length=1000, null=True)

    # related__objects = Student._meta.related_objects
    #


class StudentLetter(models.Model):
    template = models.TextField()
