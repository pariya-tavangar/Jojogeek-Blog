from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']