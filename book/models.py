from django.conf import settings
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="books")
    description = models.TextField()
