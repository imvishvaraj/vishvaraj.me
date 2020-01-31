from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from tinymce.models import HTMLField

User = get_user_model()


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    # url = models.CharField(max_length=200)
    # overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    # featured = models.BooleanField()
    previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })

    def overview(self):
        return self.content[:200]

    def post_url(self):
        day = self.timestamp.strftime('%Y-%m-%d').split("-")
        day = "_".join(day)
        post_name = "_".join(self.title.split(" ")).lower()
        return day+"_"+post_name

    @property
    def get_comments(self):
        return self.comments.all()
