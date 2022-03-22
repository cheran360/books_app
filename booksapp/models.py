from django.db import models

# Create your models here.

class Email(models.Model):
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
