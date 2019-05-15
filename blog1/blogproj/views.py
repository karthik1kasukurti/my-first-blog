from django.http import HttpResponse
from django.shortcuts import render

posts = [
	{
	'title': 'blog post 1',
	'author': 'karthik',
	'date_posted': '15 may 2019',
	},
	{
	'title': 'blog post 2',
	'author': 'linuxer',
	'date_posted': '14 may 2019',
	}
]

def home_page(request):
	context = 	{'posts': posts}
	
	return render(request, 'blog1/home.html', context)

#def home_page(request):
#	my_title="hello there.."
#	return render(request,"hello_world.html",{"title": my_title})  #for dynamically replacing {{title}} 
	# 															in hello_world.html we use {} i.e. dictionary

def aboutus(request):
	return render(request,"blog1/about.html", {"title":"About"})

# def home_page(request):
# 	return HttpResponse("<h1>hello world</h1>")

# def aboutus(request):
# 	return HttpResponse("<h1>about page</h1>")	