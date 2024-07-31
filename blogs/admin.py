from django.contrib import admin

from blogs.models import Blog, Author


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'auther_id', 'image']
    list_display = ('title', 'slug', 'date_added')
    list_filter = ('title', 'date_added')
    search_fields = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'education')
    list_filter = ('full_name', 'education')
    search_fields = ('full_name',)
