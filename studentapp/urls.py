from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('',views.studenthome),
    path('courselist3/',views.courselist3),
    path('batchlist2/',views.batchlist2),
    path('admission/',views.admission),
    path('batchstatus/',views.batchstatus),
    path('logout2/',views.logout2),
    
    
]