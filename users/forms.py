from django import forms
from .models import order

class orderForm(forms.ModelForm):

	class Meta:
		model = order
		fields = ('profile_link','picture_link','likes_Quantity','followers_Quantity','discount','infos')