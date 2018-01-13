from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm
from .forms import RegisterForm
from .forms import LoginForm

def home_page(request):
    context={
        "title":"Home Page!",
        "content":"Welcome to the Home Page!"
    }
    if request.user.is_authenticated():
        context[ "premiumContent" ]= "I am premium now :)"
    return render(request,"home.html",context)

def about_page(request):
    context={
        "title":"About Page!",
        "content":"Welcome to the About Page!"
    }
    return render(request,"home.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context={
        "title":"Contact Page!",
        "content":"Welcome to the Contact Page!",
        "form"  : contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if (request.method == "POST"):
    #     print(request.POST.get('fullName'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('message'))
    return render(request,"contact/view.html",context)


def login_page(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    print(request.user.is_authenticated())


    if form.is_valid():
        print(form.cleaned_data)
        context['form'] = LoginForm()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        print(request.user.is_authenticated())
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print('Error')
    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        newUser =  User.objects.create_user(username,email,password)
        print(newUser)
    return render(request,"auth/register.html",context)


