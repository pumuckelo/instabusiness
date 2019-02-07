from django import forms
from .models import order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



#form for new orders
class orderForm(forms.ModelForm):

	class Meta:
		model = order
		fields = ('profile_link','picture_link','likes_Quantity','followers_Quantity','discount','infos')


#form for registration
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')


