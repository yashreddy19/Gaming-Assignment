from django.db import models
import uuid


# Create your models here.
class Game(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
