from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('update/<str:pk>', views.updatePhoto, name='update'),
    path('delete/<str:pk>', views.deletePhoto, name='delete'),
    

]