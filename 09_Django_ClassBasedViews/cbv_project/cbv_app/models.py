from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name = "students", on_delete = models.CASCADE)
    #! the related_name parameter is important for linking the contents of student and school in the html tag
    #! see school_detail.students.all in school_detail.html

    def __str__(self):
        return self.name