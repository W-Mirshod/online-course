from django.urls import path
from blogs.views import BlogsPage, SinglePage, AddComment

urlpatterns = [
    path('', BlogsPage.as_view(), name='blog'),
    path('single/<slug:slug>', SinglePage.as_view(), name='single'),
    path('add_comment/<slug:slug>/', AddComment.as_view(), name='add_comment_blog'),
]
