from django import forms
from .models import order_like, order_follower
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



#form for new orders
class orderForm(forms.ModelForm):

	class Meta:
		model = order_follower
		fields = ('profile_link','follower','discount','infos',)


#form for registration
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2',)


