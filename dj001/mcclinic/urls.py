from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('about/doctors', views.doctors, name='doctors'),
    path('about/doctors/doctor_page/', views.doctor_page, name='doctor_page'),
    path('about/contacts', views.contacts, name='contacts'),
    path('about/docsl', views.docsl, name='docsl'),
    path('about/insurance', views.insurance, name='insurance'),
    path('about/job', views.job, name='job'),
    path('about/promo', views.promo, name='promo'),
    path('about/services', views.services, name='services'),
    path('about/analyzes', views.analyzes, name='analyzes'),
    path('about/analyzes_price', views.analyzes_price, name='analyzes_price'),
    
        
]
