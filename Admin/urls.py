"""
URL configuration for ExaminationSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from .import views
urlpatterns = [
       path('login/',views.admin_login,name='adminlogin'),
       path('dash/',views.admin_dashboard,name='admindash'),
       path('addtr/',views.add_teacher,name='addtr'),
       path('viewtr/',views.view_teacher,name='viewtr'),
       path('edittr/<int:id>/',views.edit_teacher,name='edittr'),
       path('deletetr/<int:id>/',views.delete_teacher,name='deletetr'),
       path('viewstd/',views.view_student,name='viewstd'),
       path('editstd/<int:id>/',views.edit_student,name='editstd'),
       path('deletestd/<int:id>/',views.delete_student,name='deletestd'),
]
