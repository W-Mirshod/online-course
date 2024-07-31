from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from blogs.models import Blog
from courses.forms import CommentForm
from courses.models import Course, Category, Comment
from teachers.models import Teacher


class IndexPage(View):
    def get(self, request):
        categories = Category.objects.order_by('-created_at')[:4]
        comments = Comment.objects.order_by('-created_at')[:5]
        teachers = Teacher.objects.order_by('-created_at')[:4]
        courses = Course.objects.order_by('-created_at')[:8]
        blogs = Blog.objects.order_by('-created_at')[:3]

        context = {'categories': categories,
                   'teachers': teachers,
                   'comments': comments,
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
        search = request.GET.get('search_query')

        if search:
            course = Course.objects.filter(title__icontains=search)
        else:
            course = Course.objects.all()

        context = {'categories': categories,
                   'courses': course,
                   'active_page': 'courses'}

        return render(request, 'courses/course.html', context)


class AddComment(View):
    def get(self, request, slug):
        form = CommentForm()
        return render(request, 'courses/course_detail.html', {'form': form, 'slug': slug})

    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            course_id = get_object_or_404(Course, slug=slug)

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']
            media_file = form.cleaned_data['media_file']

            comment = Comment(name=name, email=email, rating=rating, comment=comment, course_id=course_id)
            if media_file:
                comment.media_file = media_file

            comment.save()

            return redirect('c_detail', slug=slug)
        return redirect('c_detail', slug=slug)


class DeleteComment(View):
    def get(self, request, slug):
        comment_id = request.GET.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('c_detail', slug=slug)


class ContactPage(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {'categories': categories,
                   'active_page': 'contact'}

        return render(request, 'info/contact.html', context)


class AboutPage(View):
    def get(self, request):
        comments = Comment.objects.order_by('-created_at')[:5]
        categories = Category.objects.all()

        context = {'comments': comments,
                   'categories': categories,
                   'active_page': 'about'}

        return render(request, 'info/about.html', context)
