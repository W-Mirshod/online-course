from django.urls import path

from courses.views import IndexPage, CoursePage, AboutPage

urlpatterns = [
    path('home/', IndexPage.as_view(), name='index'),
    path('', CoursePage.as_view(), name='course'),
    path('about/', AboutPage.as_view(), name='about'),
]
