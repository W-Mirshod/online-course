from django.urls import path
from teachers.views import TeachersPage

urlpatterns = [
    path('', TeachersPage.as_view(), name='teacher'),
]
