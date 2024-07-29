from django.shortcuts import render
from django.views import View

from courses.models import Course, Category
from teachers.models import Teacher


class IndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()
        courses = Course.objects.all()

        context = {'categories': categories,
                   'teachers': teachers,
                   'courses': courses,
                   'active_page': 'active'}
        return render(request, 'index.html', context)


class CoursePage(View):
    def get(self, request):
        categories = Category.objects.all()
        course = Course.objects.all()

        context = {'categories': categories,
                   'courses': course}
        return render(request, 'course.html', context)


class ContactPage(View):
    def get(self, request):
        return render(request, 'contact.html')


class SinglePage(View):
    def get(self, request):
        return render(request, 'single.html')


class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')
