from django.shortcuts import render
from django.views import View


class TeacherPage(View):
    def get(self, request):
        return render(request, 'teacher.html')
