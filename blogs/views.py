from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from blogs.forms import CommentForm
from blogs.models import Blog
from courses.models import Category, Comment


class BlogsPage(View):
    def get(self, request):
        blogs = Blog.objects.all()
        categories = Category.objects.all()
        num_of_categories = len(categories)

        context = {'blogs': blogs,
                   'categories': categories,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blogs/blog.html', context)


class SinglePage(View):
    def get(self, request, slug):
        category = None
        print(slug)
        if slug == '/blog/single/None':
            category = Category.objects.get(slug=slug)

        blog = Blog.objects.get(slug=slug)
        categories = Category.objects.all()
        comments = Comment.objects.filter(blog_id__slug=slug)
        num_of_categories = len(categories)

        context = {'blog': blog,
                   'category': category,
                   'categories': categories,
                   'comments': comments,
                   'num_of_categories': num_of_categories,
                   'active_page': 'blog'}

        return render(request, 'blogs/blog_detail.html', context)


class AddComment(View):
    def get(self, request, slug):
        form = CommentForm()
        return render(request, 'blogs/blog_detail.html', {'form': form, 'slug': slug})

    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            blog_id = get_object_or_404(Blog, slug=slug)

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']
            media_file = form.cleaned_data['media_file']

            comment = Comment(name=name, email=email, rating=rating, comment=comment, blog_id=blog_id)
            if media_file:
                comment.media_file = media_file

            comment.save()

            return redirect('single', slug=slug)
        return redirect('single', slug=slug)
