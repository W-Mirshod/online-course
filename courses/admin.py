from django.contrib import admin

from courses.models import Course, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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
