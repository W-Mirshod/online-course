from django.shortcuts import render
from django.views import View

from courses.models import Course


class IndexPage(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {'courses': courses,
                   'active_page': 'active'}
        return render(request, 'index.html', context)


class CoursePage(View):
    def get(self, request):
        course = Course.objects.all()
        context = {'courses': course}
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
