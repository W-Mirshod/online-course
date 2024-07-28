from django.urls import path
from teachers.views import TeacherPage

urlpatterns = [
    path('', TeacherPage.as_view(), name='teacher'),
]
