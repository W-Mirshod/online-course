from django.urls import path
from blogs.views import BlogsPage, SinglePage, AddComment, DeleteComment

urlpatterns = [
    path('', BlogsPage.as_view(), name='blog'),
    path('single/<slug:slug>', SinglePage.as_view(), name='single'),
    path('add_comment/<slug:slug>/', AddComment.as_view(), name='add_comment_blog'),
    path('del_comment/<slug:slug>/', DeleteComment.as_view(), name='del_comment_blog'),
]
