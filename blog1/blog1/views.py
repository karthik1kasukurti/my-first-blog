from django.http import HttpResponse
from django.shortcuts import render

#def home_page(request):
#	return HttpResponse("<h3>welcome to my website's home page</h3>")

def home_page(request):
	return render(request,"hello_world.html")

def about_page(request)	:
	return HttpResponse("<h4>about us</h4>")