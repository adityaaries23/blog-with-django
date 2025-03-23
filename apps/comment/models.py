from django.db import models

from core.models import BaseModel
from apps.blog.models import Post


# Create your models here.
class Comment(BaseModel):
    content = models.TextField()
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


class ReplyComment(BaseModel):
    content = models.TextField()
    Comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply_comments')