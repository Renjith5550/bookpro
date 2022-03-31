import password as password
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta():
        model=User
        fields=["username",
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class": "form-control"}),
            "last_name":forms.TextInput(attrs={"class": "form-control"}),
            "email":forms.EmailInput(attrs={"class": "form-control"}),

        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class PasswordResetForm(forms.Form):
    oldPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    newPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data=super().clean()
        oldPassword=forms.