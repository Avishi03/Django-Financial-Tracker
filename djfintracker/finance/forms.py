from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm ):
    class Meta: #we define model in this 
        model = User
        fields = ['username', 'email', 'password1','password2']#fields already there in user 
        #but if some filed is not there then write as eg: email =forms.EmailField()