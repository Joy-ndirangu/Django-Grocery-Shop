from django.shortcuts import render, redirect
from  .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# for user registration

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterUserForm
# Create your views here.

def home(request):
    items = Product.objects.all()
    return render(request,"index.html",{'navbar':'home', 'items':items})

def about(request):
    return  render(request, "about.html", {'navbar':'about'})

def products(request):
    product = Product.objects.all()
    return render(request, "product.html", {'navbar':'products', 'product':product})

def viewdetails(request, id):
    details = Product.objects.get(id=id)
    return render(request,"viewdetail.html", {'navbar':'products', 'details':details})

def category(request, name):
    # Grab the category from the url
    try:
        category = Category.objects.get(name=name)
        cat_products = Product.objects.filter(category=category)
        return  render(request, "category.html", {'cat_products':cat_products, 'category':category})

    except:
        messages.warning(request, "That category doesn't exist")
        return  redirect('Store:home')




def blogs(request):
    return render(request, "blog.html", {'navbar':'blogs'})

def features(request):
    return render(request, "feature.html", {'navbar':'features'})

def testimonials(request):
    return render(request, "testimonial.html", {'navbar':'testimonial'})

def contact(request):
    return render(request, "contact.html", {'navbar':'contact'})

def login_user(request):
    # If user filled and posted the form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Log in successful")
            return redirect('Store:home')

        else:
            messages.warning(request, "There was an error logging in, Try again")
            return redirect('Store:signin')

    else:
        return render(request,"login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out")
    return redirect('Store:home')

def register_user(request):
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Logging in user
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "Registration successful")
            return redirect('Store:home')

        else:
            messages.success(request, "There was a problem registering, Please try again")
            return redirect('Store:signup')


    else:
        return render(request, "signup.html", {'form':form})
