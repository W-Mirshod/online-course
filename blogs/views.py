from django.shortcuts import render
from django.views import View


class BlogsPage(View):
    def get(self, request):
        context = {'active_page': 'blog'}

        return render(request, 'blog.html', context)
