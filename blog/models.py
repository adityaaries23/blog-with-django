from django.db import models

from core.models import BaseModel


# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    views = models.IntegerField(default=0)