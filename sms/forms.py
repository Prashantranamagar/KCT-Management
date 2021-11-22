from django import forms
from sms.models import Cordinator
from django.contrib.auth.models import User

class CordinatorForm(forms.ModelForm):
	class Meta:
		models = Cordinator
		fields= '__all__'




class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput,)


class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget= forms.PasswordInput,)

	class Meta: 
		model = User
		fields = ('username', 'first_name', 'last_name', 'password', 'email')