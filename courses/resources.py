from import_export import resources
from .models import Course, Category, Comment


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        exclude = []


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        exclude = []


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        exclude = []
