from django.shortcuts import render
from django.views import View


class TeachersPage(View):
    def get(self, request):
        context = {'active_page': 'teachers'}

        return render(request, 'teachers/teacher.html', context)
