from django.shortcuts import render
from django.views import View

from courses.models import Course


class IndexPage(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {'courses': courses}
        return render(request, 'index.html', context)
