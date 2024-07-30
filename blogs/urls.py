from django.urls import path

from blogs.views import BlogsPage

urlpatterns = [
    path('', BlogsPage.as_view(), name='blog'),
]
