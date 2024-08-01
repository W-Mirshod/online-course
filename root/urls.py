"""
URL configuration for root project.

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from root import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from courses.views.views import CoursesPage

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('blog/', include('blogs.urls')),
                  path('accounts/profile/', CoursesPage.as_view(), name='course'),
                  path('courses/', include('courses.urls')),
                  path('teachers/', include('teachers.urls')),
                  path('social-auth/', include('social_django.urls', namespace='social')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
