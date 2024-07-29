from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from teachers.views import TeachersPage, TeachersDetail, AddComment

urlpatterns = [
                  path('', TeachersPage.as_view(), name='teacher'),
                  path('teachers/<slug:slug>', TeachersDetail.as_view(), name='t_slug'),
                  path('add_comment/<slug:slug>/', AddComment.as_view(), name='add_comment_teacher'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
