from django.urls import path

from blogs.views import BlogsPage, SinglePage

urlpatterns = [
    path('', BlogsPage.as_view(), name='blog'),
    path('single/<slug:slug>', SinglePage.as_view(), name='single'),
]
