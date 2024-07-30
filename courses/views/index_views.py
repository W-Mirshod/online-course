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
                   'active_page': 'home'}

        return render(request, 'index.html', context)


class CoursesPage(View):
    def get(self, request):
        categories = Category.objects.all()
        course = Course.objects.all()

        context = {'categories': categories,
                   'courses': course,
                   'active_page': 'courses'}

        return render(request, 'course.html', context)


class ContactPage(View):
    def get(self, request):
        context = {'active_page': 'contact'}

        return render(request, 'contact.html', context)


class SinglePage(View):
    def get(self, request):
        context = {'active_page': 'blog'}

        return render(request, 'single.html', context)


class AboutPage(View):
    def get(self, request):
        context = {'active_page': 'about'}

        return render(request, 'about.html', context)
