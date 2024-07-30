from django.db.models import Count, Avg, Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from blogs.models import Blog
from courses.forms import CommentForm, GettingCoursesForm
from courses.models import Course, Category, Comment
from teachers.models import Teacher


class IndexPage(View):
    def get(self, request):
        user = request.user
        courses_for_purchase = None

        courses = Course.objects.annotate(average_rating=Avg('course_comments__rating'),
                                          counts_of_ratings=Sum('course_comments__rating')).order_by('-created_at')[:8]
        categories = Category.objects.order_by('-created_at')[:4]
        comments = Comment.objects.order_by('-created_at')[:5]
        teachers = Teacher.objects.order_by('-created_at')[:4]
        blogs = Blog.objects.order_by('-created_at')[:3]
        if user.is_authenticated:
            courses_for_purchase = Course.objects.exclude(bought_courses__user=user)

        context = {'categories': categories,
                   'teachers': teachers,
                   'comments': comments,
                   'courses': courses,
                   'blogs': blogs,
                   'courses_for_purchase': courses_for_purchase,
                   'active_page': 'home'}

        return render(request, 'courses/index.html', context)


class BaseIndexPage(View):
    def get(self, request):
        categories = Category.objects.annotate(course_count=Count('courses'))
        courses = Course.objects.annotate(average_rating=Avg('course_comments__rating'),
                                          counts_of_ratings=Sum('course_comments__rating'))

        context = {'categories': categories,
                   'courses': courses, }

        return render(request, 'base.html', context)


class CoursesPage(View):
    def get(self, request):
        categories = Category.objects.annotate(course_count=Count('courses'))
        courses = Course.objects.annotate(average_rating=Avg('course_comments__rating'),
                                          counts_of_ratings=Sum('course_comments__rating'))
        search = request.GET.get('search_query')

        if search:
            course = Course.objects.filter(title__icontains=search)
        else:
            course = Course.objects.all()

        context = {'categories': categories,
                   'courses': courses,
                   'active_page': 'courses'}

        return render(request, 'courses/course.html', context)


class AddComment(View):
    def get(self, request, slug):
        form = CommentForm()
        return render(request, 'courses/course_detail.html', {'form': form, 'slug': slug})

    def post(self, request, slug):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            course_id = get_object_or_404(Course, slug=slug)

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']
            media_file = form.cleaned_data['media_file']

            if media_file:
                comment = Comment(name=name, email=email, rating=rating, comment=comment, course_id=course_id,
                                  media_file=media_file)

            else:
                comment = Comment(name=name, email=email, rating=rating, comment=comment, course_id=course_id)
            comment.save()

            return redirect('c_detail', slug=slug)
        return redirect('c_detail', slug=slug)


class DeleteComment(View):
    def get(self, request, slug):
        comment_id = request.GET.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('c_detail', slug=slug)


class GettingCourses(FormView):
    template_name = 'courses/index.html'
    form_class = GettingCoursesForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactPage(View):
    def get(self, request):
        categories = Category.objects.annotate(course_count=Count('courses'))

        context = {'categories': categories,
                   'active_page': 'contact'}

        return render(request, 'info/contact.html', context)


class AboutPage(View):
    def get(self, request):
        comments = Comment.objects.order_by('-created_at')[:5]
        categories = Category.objects.annotate(course_count=Count('courses'))

        context = {'comments': comments,
                   'categories': categories,
                   'active_page': 'about'}

        return render(request, 'info/about.html', context)
