from django.shortcuts import render
from django.views import View

from courses.models import Category


class TeachersPage(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {'active_page': 'teachers',
                   'categories': categories}

        return render(request, 'teachers/teacher.html', context)
