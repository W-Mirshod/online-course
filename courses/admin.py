from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from courses.models import Course, Category, Comment, User
from courses.resources import CategoryResource, CourseResource, CommentResource


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CategoryResource

    fields = ['title', 'image']
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CourseResource

    fields = ['title', 'description', 'number_of_students', 'price',
              'duration', 'teachers', 'category', 'video']
    list_display = ('title', 'slug', 'number_of_students', 'price')
    search_fields = ('title', 'teachers')
    list_filter = ('duration', 'price')


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CommentResource

    fields = ['name', 'email ', 'comment', 'is_published', 'rating', 'created_at', 'course_id', 'blog_id', 'author_id']
    list_display = ('name', 'email', 'comment', 'is_published', 'rating', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('is_published', 'rating', 'created_at')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
