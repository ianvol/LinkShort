from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    long_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    def __str__(self):
        return self.short_url
   
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

