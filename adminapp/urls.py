from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminhome),  
    path('addcourse/',views.addcourse),
    path('courselist1/',views.courselist1),
    path('studentlist/',views.studentlist),
    path('batchentry1/',views.batchentry1),
    path('editcourse/',views.editcourse),
    path('admissionstatus/',views.admissionstatus),
    path('logout1/',views.logout1),
]
