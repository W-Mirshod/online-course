from django.db.models import Q
from django.shortcuts import render
from django.views import View
from courses.models import Category
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

        context = {'teacher': teacher,
                   'categories': categories, }

        return render(request, 'teachers/teacher_detail.html', context)
