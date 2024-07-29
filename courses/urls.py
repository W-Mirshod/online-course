from django.urls import path

from courses.views import IndexPage, CoursePage, ContactPage, SinglePage, AboutPage

urlpatterns = [
    path('home/', IndexPage.as_view(), name='index'),
    path('', CoursePage.as_view(), name='course'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('single/', SinglePage.as_view(), name='single'),
    path('about/', AboutPage.as_view(), name='about'),
]
