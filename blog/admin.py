from django.contrib import admin
from .models import Post

# adding post model into admin panel
admin.site.register(Post)
