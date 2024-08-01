from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from courses.models import Category, Comment
from teachers.forms import CommentForm
from teachers.models import Teacher


class TeachersPage(View):
    def get(self, request):
        categories = Category.objects.all()
        search = request.GET.get('search_query')

        if search:
            teachers = Teacher.objects.filter(
                Q(full_name__icontains=search) | Q(twitter_link__icontains=search) | Q(facebook_link__icontains=search))
        else:
            teachers = Teacher.objects.all()

        context = {'teachers': teachers,
                   'active_page': 'teachers',
                   'categories': categories}

        return render(request, 'teachers/teacher.html', context)


class TeachersDetail(View):
    def get(self, request, slug):
        teacher = Teacher.objects.get(slug=slug)
        categories = Category.objects.all()
        comments = Comment.objects.filter(teacher_id=teacher.id).order_by('-created_at')

        context = {'teacher': teacher,
                   'comments': comments,
                   'categories': categories, }

        return render(request, 'teachers/teacher_detail.html', context)


class AddComment(View):
    def get(self, request, slug):
        form = CommentForm()
        return render(request, 'teachers/teacher_detail.html', {'form': form, 'slug': slug})

    def post(self, request, slug):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            teacher_id = get_object_or_404(Teacher, slug=slug)

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']
            media_file = form.cleaned_data['media_file']

            if media_file:
                comment = Comment(name=name, email=email, rating=rating, comment=comment, teacher_id=teacher_id,
                                  media_file=media_file)
            else:
                comment = Comment(name=name, email=email, rating=rating, comment=comment, teacher_id=teacher_id)

            comment.save()

            return redirect('t_slug', slug=slug)
        return redirect('t_slug', slug=slug)


class DeleteComment(View):
    def get(self, request, slug):
        comment_id = request.GET.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('t_slug', slug=slug)
