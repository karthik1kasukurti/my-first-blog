from django.urls import path
from . import views

urlpatterns = [
	#path('page/',about_page),
	#path('pages/',about_page),
	
	#re_path(r'^pages?/$',about_page),	#this is same as combination of above two lines
	path('', views.home_page, name='blog-home'),
	path('home/', views.home_page, name='blog-home'),
	path('about/', views.aboutus, name='blog-about'),
    
]