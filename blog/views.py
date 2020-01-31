from django.shortcuts import render


def blogpage(request):
    return render(request, 'blog/blog.html')


def post(request):
    return render(request, 'blog/post.html')