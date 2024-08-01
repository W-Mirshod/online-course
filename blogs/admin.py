from django.contrib import admin

from blogs.models import Blog, Author


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'auther_id', 'content', 'image']
    list_display = ('title', 'slug', 'created_at')
    list_filter = ('title', 'created_at')
    search_fields = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'education')
    list_filter = ('full_name', 'education')
    search_fields = ('full_name',)
