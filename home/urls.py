#urls of homepage of ecoomerce app
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('about',views.about,name='about'),
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('success/', views.success, name='success'),
    path('home',views.home,name='home'),
    path('project/face-recognition/', views.face_recognition_view, name='face_recognition'),
    path('project/virtual-ai/', views.virtual_ai_view, name='virtual_ai'),
    path('project/stock-data/', views.stock_data_view, name='stock_data'),
    path('project/resume-showcase/', views.resume_showcase_view, name='resume_showcase'),
    path('project/disease-detection/', views.disease_detection_view, name='disease_detection'),
    path('project/youtube-instagram-scraper/', views.youtube_instagram_scraper_view, name='youtube_instagram_scraper')
    path('run-migrations/', run_migrations, name='run_migrations')

    
    
]
