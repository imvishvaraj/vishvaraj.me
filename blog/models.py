from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    # next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    # url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "posts"
