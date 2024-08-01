from django.db.models import Count
from django.shortcuts import render
from django.views import View
from blogs.models import Blog
from courses.models import Course, Category, Comment


class CourseDetailPage(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        comments = Comment.objects.filter(course_id__slug=slug).order_by('-created_at')
        categories = Category.objects.all()
        blogs = Blog.objects.all()

        context = {'course': course,
                   'comments': comments,
                   'categories': categories,
                   'blogs': blogs, }

        return render(request, 'courses/course_detail.html', context)


class CategoryDetailPage(View):
    def get(self, request, slug):
        category = None
        if Category.objects.filter(slug=slug).exists():
            category = Category.objects.filter(slug=slug).annotate(course_count=Count('courses'))
        categories = Category.objects.annotate(course_count=Count('courses'))
        print(categories)
        print(categories)
        print(categories)
        print(categories)
        category_videos = Course.objects.filter(category=category)
        blogs = Blog.objects.all()

        context = {'category': category,
                   'categories': categories,
                   'category_videos': category_videos,
                   'blogs': blogs, }

        return render(request, 'courses/category_detail.html', context)
