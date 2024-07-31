from import_export import resources
from .models import Blog, Author


class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog
        exclude = []


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author
        exclude = []
