
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your forms here.

class NewUserForm(UserCreationForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Confirm Password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	email = forms.CharField(required = True, widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))


	class Meta:
		model = User
		fields = ("username",  "first_name", "last_name", "email", "password1", "password2")
		labels = {'email': 'Email'}
		widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
		
    


