from django.urls import path

from courses.views.index_views import IndexPage, CoursePage, ContactPage, SinglePage, AboutPage
from courses.views.authentication import AuthenticationView

urlpatterns = [
    # index
    path('home/', IndexPage.as_view(), name='index'),
    path('', CoursePage.as_view(), name='course'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('single/', SinglePage.as_view(), name='single'),
    path('about/', AboutPage.as_view(), name='about'),

    # auth
    path('auth/', AuthenticationView.as_view(), name='auth'),
]
