from django.urls import is_valid_path, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('expertise', views.expertise, name='expertise'),
    path('cases', views.cases, name='cases'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('team', views.team, name='team'),
    path('blog', views.blog, name='blog'),
    path('contactus', views.contactus, name='contactus'),
    path('team/detail/<str:pk>', views.teamdetail, name='teamdetail'),
    path('expertise/detail/<str:pk>', views.expertisedetail, name='expertisedetail'),
    path('blog/detail/<str:pk>', views.blogdetail, name='blogdetail')
]