from django.urls import path

from courses.views.views import IndexPage, CoursesPage, ContactPage, AboutPage, BaseIndexPage, CDetailPage, CGDetailPage
from courses.views.authentication import SignUpView, LogInView

urlpatterns = [
    # index
    path('home/', IndexPage.as_view(), name='index'),
    path('', CoursesPage.as_view(), name='course'),
    path('', BaseIndexPage.as_view(), name='base'),
    path('course/<slug:slug>/', CDetailPage.as_view(), name='c_detail'),
    path('category/<slug:slug>/', CGDetailPage.as_view(), name='cg_detail'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('about/', AboutPage.as_view(), name='about'),

    # auth
    path('sign-in/', LogInView.as_view(), name='sign_in'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
]
