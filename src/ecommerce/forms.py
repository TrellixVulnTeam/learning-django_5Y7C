from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()
class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
            attrs={"class":"form-control",
                   "placeHolder":"Name",
                   "name":"fullName"
                   }))
    email    = forms.EmailField( widget=forms.EmailInput(
        attrs={"class":"form-control",
               "placeHolder":"Email",
               "name":"email"
               }))
    message  = forms.CharField( widget=forms.Textarea(
        attrs={"class":"form-control",
               "placeHolder":"Your message",
               "name":"message"
               }))


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email

    def clean_name(self):
        name = self.cleaned_data.get("name")
        while name == "" or any(str.isdigit(c) for c in name):
            raise forms.ValidationError("Name cannot contain numbers!")

        return name


class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm Password')
    email     = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2 :
            raise forms.ValidationError("Passwords must match")

        return data
