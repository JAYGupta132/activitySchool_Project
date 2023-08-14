from django.contrib import admin
from django.urls import path,include
from . import views

# for file uploading ...
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register/', views.register),
    path('login/', views.login),
    path('gallery/', views.gallery),
    path('courselist2/', views.courselist2),
    path('adminhome/', include('adminapp.urls')),
    path('studenthome/', include('studentapp.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
