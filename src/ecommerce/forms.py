from django import forms

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