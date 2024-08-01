from django.db.models import Count
from django.shortcuts import render
from django.views import View
from blogs.models import Blog
from courses.models import Course, Category, Comment


class CourseDetailPage(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        comments = Comment.objects.filter(course_id__slug=slug).order_by('-created_at')
        categories = Category.objects.annotate(course_count=Count('courses'))
        blogs = Blog.objects.all()

        context = {'course': course,
                   'comments': comments,
                   'categories': categories,
                   'blogs': blogs, }

        return render(request, 'courses/course_detail.html', context)


class CategoryDetailPage(View):
    def get(self, request, slug):
        categories = Category.objects.annotate(course_count=Count('courses'))
        category = None
        if Category.objects.filter(slug=slug).exists():
            category = Category.objects.filter(slug=slug).annotate(course_count=Count('courses'))
        category_videos = Course.objects.filter(category=category)
        blogs = Blog.objects.all()

        context = {'category': category,
                   'categories': categories,
                   'category_videos': category_videos,
                   'blogs': blogs, }

        return render(request, 'courses/category_detail.html', context)


class StudentRoomPage(View):
    def get(self, request):
        user = request.user
        courses = Course.objects.filter(bought_courses__user=user)
        comments = Comment.objects.filter(email__icontains=user.email).order_by('-created_at')
        categories = Category.objects.annotate(course_count=Count('courses'))

        context = {'courses': courses,
                   'comments': comments,
                   'categories': categories, }

        return render(request, 'others/student_page.html', context)
