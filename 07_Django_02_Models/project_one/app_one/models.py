from django.db import models

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    # max_lenght is a constraint on the length of the field
    # unique=True means that there shouldn't be any duplicates (all the topics must be unique)
    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    # create 3 class object attributes
    # attributes are columns in the table "Webpage"
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
