from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Meme(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True, blank=False, editable=True, upload_to='static/images')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='memes')

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_updated_at(self):
        return self.updated_at
