from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import BlogsPage, SinglePage, AddComment, DeleteComment, BlogDetail

urlpatterns = [
                  path('', BlogsPage.as_view(), name='blog'),
                  path('single/', SinglePage.as_view(), name='single_1'),
                  path('blog_detail/<slug:slug>/', BlogDetail.as_view(), name='single'),
                  path('add_comment/<slug:slug>/', AddComment.as_view(), name='add_comment_blog'),
                  path('del_comment/<slug:slug>/', DeleteComment.as_view(), name='del_comment_blog'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
