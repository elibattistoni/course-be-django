from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    #! you need a method that allows you to redirect to a URL
    #! this is a specific name for a django method
    def get_absolute_url(self):
        return reverse("cbv_app:school_detail", kwargs={"pk":self.pk})

class Student(models.Model):
    name = models.CharField(max_length = 256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name = "students", on_delete = models.CASCADE)
    #! the related_name parameter is important for linking the contents of student and school in the html tag
    #! see school_detail.students.all in school_detail.html

    def __str__(self):
        return self.name