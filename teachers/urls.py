from django.urls import path
from teachers.views import TeachersPage, TeachersDetail

urlpatterns = [
    path('', TeachersPage.as_view(), name='teacher'),
    path('teachers/<slug:slug>', TeachersDetail.as_view(), name='t_slug'),
]
