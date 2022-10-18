"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from course.views import create_course, create_homework
from familiar.views import create_familiar
from profesor.views import create_profesor
from student.views import create_student


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path(
        "create_familiar/<str:name>/<str:last_name>/<str:kin>/<str:email>/<str:birth_day>",
        create_familiar,
    ),

    path("familiar/", include("familiar.urls")),
]
