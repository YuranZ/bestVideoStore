from django.db import models

class Video(models.Model):
    urls = models.URLField()
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    likes = models.PositiveIntegerField(default=0)

class Comment (models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment_video = models.ForeignKey(Video, on_delete=models.CASCADE)

# Create your models here.
