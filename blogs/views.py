from django.shortcuts import render
from django.views import View

from blogs.models import Blog


class BlogsPage(View):
    def get(self, request):
        blogs = Blog.objects.all()

        context = {'blogs': blogs,
                   'active_page': 'blog'}

        return render(request, 'blogs/blog.html', context)
