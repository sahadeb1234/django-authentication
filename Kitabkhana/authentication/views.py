from django.shortcuts import render
from django.contrib.auth import forms
from django.shortcuts import render, HttpResponseRedirect
from .forms import NewUserForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout

from .models import(
   SliderImage
)
# Create your views here.
def index(request):
	 images = SliderImage.objects.all()
	 return render(request, 'authentication/index.html', {'images':images})

def customerregistration(request):
	if request.method =='POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			messages.success
			form.save()
			form =NewUserForm()
	else:
		form =NewUserForm()	
	return  render(request,'authentication/customerregistration.html', {'form':form})

def userlogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect("/profil/")
	form = AuthenticationForm()
	return render(request, 'authentication/login.html', {'form':form})

# def logout(request):
# 	 return render(request, 'authentication/logout.html')
def loginout(request):
	logout(request)
def profil(request):
	return render (request, "authentication/profil.html")


#change password

def passwordchange(request):
	if request.method =="POST":
		fm = PasswordChangeForm(user=request.user, data=request.POST)
		if fm.is_valid():
			fm.save()
			return HttpResponseRedirect(request, "authentication/profil.html")
	else:
		fm = PasswordChangeForm(user=request.user)
	return render (request, "authentication/changepw.html", {'form':fm})


	# class ProductView(View):
	# 	return render(request, 'app/home.html')




