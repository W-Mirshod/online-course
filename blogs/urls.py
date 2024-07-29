from django.urls import path

from blogs.views import BlogPage

urlpatterns = [
    path('', BlogPage.as_view(), name='blog'),
]
