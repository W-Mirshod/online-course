from django.shortcuts import render
from django.views import View
from courses.models import Course, Category, Comment
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

        return render(request, 'courses/index.html', context)


class BaseIndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories, }

        return render(request, 'base.html', context)


class CoursesPage(View):
    def get(self, request):
        categories = Category.objects.all()
        course = Course.objects.all()

        context = {'categories': categories,
                   'courses': course,
                   'active_page': 'courses'}

        return render(request, 'courses/course.html', context)


class CDetailPage(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        categories = Category.objects.all()

        context = {'course': course,
                   'categories': categories}

        return render(request, 'courses/detail.html', context)


class ContactPage(View):
    def get(self, request):
        context = {'active_page': 'contact'}

        return render(request, 'info/contact.html', context)


class AboutPage(View):
    def get(self, request):
        comments = Comment.objects.all()

        context = {'comments': comments,
                   'active_page': 'about'}

        return render(request, 'info/about.html', context)

# from django.views.generic import TemplateView
#
# class MyView(TemplateView):
#     template_name = 'my_template.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['site_name'] = 'My Awesome Site'
#         context['user_name'] = 'John Doe'
#         return context
