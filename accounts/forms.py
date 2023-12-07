from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    
    last_name = forms.CharField(max_length=200)

    email = forms.EmailField()

    user_name = forms.CharField(max_length=300)

    password_1 = forms.CharField(max_length=200, widget=forms.PasswordInput)
    
    password_2 = forms.CharField(max_length=200, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["user_name"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("this usernam is exists.")
        
        return username
    
    def clean_password_2(self):
        pass1 = self.cleaned_data["password_1"]
        pass2 = self.cleaned_data["password_2"]
        
        if pass1!=pass2:
            raise forms.ValidationError("pass1 not equal pass2")
        
        return pass1
    
    def clean_email(self):
        email =self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email is exists.")
        
        return email
    



class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200,widget=forms.PasswordInput)
