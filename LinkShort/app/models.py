# models.py

from django.db import models
from django.utils import timezone

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_url
