from datetime import datetime

from django.db import models


# Create your models here.
class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    count = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.subject


