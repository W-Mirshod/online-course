from import_export import resources
from .models import Teacher


class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher
        exclude = []
