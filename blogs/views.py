from django.shortcuts import render
from django.views import View
from blogs.models import Blog
from courses.models import Category


class BlogsPage(View):
    def get(self, request):
        blogs = Blog.objects.all()
        categories = Category.objects.all()
        num_of_categories = len(categories)

        context = {'blogs': blogs,
                   'categories': categories,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blogs/blog.html', context)


class SinglePage(View):
    def get(self, request):
        categories = Category.objects.all()
        num_of_categories = len(categories)

        context = {'categories': categories,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blogs/blog_detail.html', context)
