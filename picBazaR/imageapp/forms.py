from django import forms 
from . models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

	

# class EditProfileForm(forms.ModelForm): 

# 	class Meta: 
# 		model = UserProfile
# 		fields = ['first_name','last_name','socal_link','ph_no','description']  
# 		labels = {'description':'Descriptios' , 'Handel':'socal_link' , 'Ph No':'ph_no'}

class SignUpForm(UserCreationForm):
	password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		labels = {'email':'Email','first_name':'First_Name','last_name':'Last_name'}