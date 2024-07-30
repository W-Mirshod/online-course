from django.urls import path

from courses.views.index_views import IndexPage, CoursesPage, ContactPage, SinglePage, AboutPage, BaseIndexPage
from courses.views.authentication import AuthenticationView

urlpatterns = [
    # index
    path('home/', IndexPage.as_view(), name='index'),
    path('', CoursesPage.as_view(), name='course'),
    path('', BaseIndexPage.as_view(), name='base'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('single/', SinglePage.as_view(), name='single'),
    path('about/', AboutPage.as_view(), name='about'),

    # auth
    path('auth/', AuthenticationView.as_view(), name='auth'),
]
