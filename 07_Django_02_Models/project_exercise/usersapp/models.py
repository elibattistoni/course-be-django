from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50, default="DEFAULT_NAME")
    last_name = models.CharField(max_length=50, default="DEFAULT_SURNAME")
    email = models.EmailField(max_length=254, blank=False, default="DEFAULT_EMAIL@GMAIL.COM")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
