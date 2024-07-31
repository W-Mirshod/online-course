from django.contrib import admin
from teachers.models import Teacher
from teachers.resources import TeacherResource
from import_export.admin import ImportExportModelAdmin


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TeacherResource

    fields = ['full_name', 'description', 'level', 'twitter_link', 'facebook_link', 'linkedin_link', 'image']
    list_display = ('full_name', 'slug', 'level', 'description')
    search_fields = ('full_name',)
    list_filter = ('full_name', 'level')
