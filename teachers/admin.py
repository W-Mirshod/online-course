from django.contrib import admin

from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'rating')
    search_fields = ('full_name', 'email')
    list_filter = ('full_name', 'phone')
