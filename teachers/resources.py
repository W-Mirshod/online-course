from .models import Teacher
from import_export import resources


class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher
        exclude = []
