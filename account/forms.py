from tkinter import Widget
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'id':"fullName",
            'name':"first_Name",
            'required':"",
        })
        self.fields["username"].widget.attrs.update({
            'type':"text",
            'class':"form-control",
            'id':"fullName",
            'name':"username",
            'required':"",
        })
        self.fields["email"].widget.attrs.update({
            'type':"email",
            'class':"form-control",
            'id':"email",
            'name':"email",
            'aria-describedby':"emailHelp",
            'required':"",
        })
        self.fields["password"].widget.attrs.update({
            'type':"password", 
            'class':"form-control", 
            'id':"password", 
            'name':"password", 
            'required':"",
        })
        self.fields["password2"].widget.attrs.update({
            'type':"password", 
            'class':"form-control", 
            'id':"confirmPassword", 
            'name':"confirmPassword", 
            'required':"",
        })



    password = forms.CharField(label='Password')
    password2 = forms.CharField(label='Password')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match")
        return cd['password2']


class LoginForm(forms.Form):
 username = forms.CharField()
 password = forms.CharField(widget=forms.PasswordInput)



