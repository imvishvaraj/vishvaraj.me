from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'blog_entries'
    ordering = ['-date']
    paginate_by = 5


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'content', 'first_img', 'first_img_caption']

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        return super().form_valid(form)
