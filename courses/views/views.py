from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView

from blogs.models import Blog
from courses.forms import CommentForm
from courses.models import Course, Category, Comment
from teachers.models import Teacher


class IndexPage(View):
    def get(self, request):
        categories = Category.objects.order_by('-created_at')[:4]
        teachers = Teacher.objects.order_by('-created_at')[:4]
        courses = Course.objects.order_by('-created_at')[:8]
        blogs = Blog.objects.order_by('-created_at')[:3]

        context = {'categories': categories,
                   'teachers': teachers,
                   'courses': courses,
                   'blogs': blogs,
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


class AddComment(View):
    def get(self, request):
        form = CommentForm()
        return render(request, 'courses/course_detail.html', {'form': form})

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.POST.get('name')
            comment.email = request.POST.get('email')
            comment.comment = request.POST.get('comment')
            comment.rating = request.POST.get('rating')
            comment.save()

            return redirect('course')


class ContactPage(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {'categories': categories,
                   'active_page': 'contact'}

        return render(request, 'info/contact.html', context)


class AboutPage(View):
    def get(self, request):
        comments = Comment.objects.all()
        categories = Category.objects.all()

        context = {'comments': comments,
                   'categories': categories,
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
