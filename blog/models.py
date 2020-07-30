from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_img_ext_url = models.URLField(max_length=255, null=True, blank=True)
    first_img = models.ImageField(upload_to='posts_imgs/%y/', max_length=255, null=True, blank=True)
    first_img_caption = models.TextField(max_length=300, null=True, blank=True)
    slug = models.SlugField(max_length=255, editable=False, default='')
    # previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    # next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    # url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug, 'pk': self.pk})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "posts"
