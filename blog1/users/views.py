from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST) #creating instance of UserCreationForm
		if form.is_valid():
			form.save() #saves the details of the created user and we can see them from admin page
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('blog-home')
	else:
		form = UserRegisterForm()			
	return render(request, 'users/register.html', {'form': form})