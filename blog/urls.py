from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, PostView, CreatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('post/<slug:slug>', PostView.as_view(), name='post_detail'),
    # path('create_post/', CreatePostView.as_view(success_url='blog_home'), name='create_post'),
    path('accounts/', include('users.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
