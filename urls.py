"""
URL configuration for project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from .views import task
from .views import get_sign_one
app_name = 'myapp'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('signs_2/<str:sign>', views.signs_2, name='sign.2'),
    path('get_signs/<int:sign>', views.get_sign_info_by_num),
    path('get_signs/<str:sign>', views.get_sign_info),
    path('signs_3/', views.signs_3, name='sign.3'),
    path('get_sign_one/<int:sign>', views.get_sign_one, name='get_sign_one'),
    path('show_all/', views.show_all, name='signs'),
    path('task/', task, name='task'),
    path('form/', views.form, name='form'),
]
