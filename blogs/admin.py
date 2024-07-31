from django.contrib import admin
from blogs.models import Blog, Author
from import_export.admin import ImportExportModelAdmin
from blogs.resources import BlogResource, AuthorResource


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BlogResource

    fields = ['title', 'auther_id', 'content', 'image']
    list_display = ('title', 'slug', 'created_at')
    list_filter = ('title', 'created_at')
    search_fields = ('title',)


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AuthorResource

    list_display = ('full_name', 'education')
    list_filter = ('full_name', 'education')
    search_fields = ('full_name',)
