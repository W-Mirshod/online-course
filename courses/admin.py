from django.contrib import admin

from courses.models import Course, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'image']
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'number_of_students', 'price',
              'duration', 'teachers', 'category', 'video', 'image']
    list_display = ('title', 'slug', 'number_of_students', 'price')
    search_fields = ('title', 'teachers')
    list_filter = ('duration', 'price')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['name', 'email ', 'comment', 'is_published', 'rating', 'written', 'course_id', 'blog_id', 'author_id', ]
    list_display = ('name', 'email', 'comment', 'is_published', 'rating', 'written')
    search_fields = ('name', 'email')
    list_filter = ('is_published', 'rating', 'written')
