import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from  .models import Product, Category, Testimonial, Blog, Features, AddMessage, Order, Customer, orderItem, shippingAddress
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
    feedback = Testimonial.objects.all()
    article = Blog.objects.all()
    hfeature = Features.objects.all()
    return render(request,"index.html",{'navbar':'home', 'items':items, 'feedback': feedback, 'article': article, 'hfeature': hfeature})

def about(request):
    feature_data = Features.objects.all()
    return  render(request, "about.html", {'navbar':'about','feature_data': feature_data})

def products(request):
    product = Product.objects.all()
    reviews = Testimonial.objects.all()
    return render(request, "product.html", {'navbar':'products', 'product':product, 'reviews':reviews})

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
    blog = Blog.objects.all()
    return render(request, "blog.html", {'navbar':'blogs', 'blog':blog})


# to view contents of a particular blog create a blogcpntent page
def blogcontent(request, id):
    blg = Blog.objects.get(id=id)
    return render(request, "blogcontent.html",{'navbar':'blogs','blg':blg})


def features(request):
    feature = Features.objects.all()
    return render(request, "feature.html", {'navbar':'features', 'feature': feature})


# to view contents of a particular feature create a featuredetail page
def featuredetails(request, id):
    read_more = Features.objects.get(id=id)
    return render(request, "featuredetail.html", {'navbar':'feature', 'read_more':read_more})


def testimonials(request):
    testimonies = Testimonial.objects.all()
    return render(request, "testimonial.html", {'navbar':'testimonial','testimonies':testimonies})

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


# Inserting contact us msg to db

def sendmessage(request):
    # verifying if form method is post
    if request.method == "POST":
        # if yes gets the user input  and stores them  in a variable ith the same exact name as the input
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message= request.POST.get("msg")


        # creating a variable that matches the columns in the model Students with the variable names we have above
        query = AddMessage(name=name, email=email, subject=subject, message=message)
        # after comparing save everything in query using save()method
        query.save()

        # for alerts. Message below shows if saved successfully

        messages.success(request, "Message sent  successfully")

        return redirect("/contact")
    return redirect("/contact")
    # make sure to call this function in the form action attribute.
    # pass the insertdata path to it

# Searching a site

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if query:
            prod = Product.objects.filter(name__icontains=query)
            feat = Features.objects.filter(title__icontains=query)
            article = Blog.objects.filter(title__icontains=query)
            return render(request, "search.html", {'prod':prod, 'feat':feat, 'article':article})


# for cart
def cart(request):
    # authenticated user
    if request.user.is_authenticated:
        customer = request.user.customer
        # getting the order and creating it if it doesn't exist using .get_or_create()'
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'cart.html', context)

def checkout(request):
    # authenticated user
    if request.user.is_authenticated:
        customer = request.user.customer
        # getting the order and creating it if it doesn't exist using .get_or_create()'
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:' , action)
    print('Product:', productId)

    # creating customer
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderitem, created = orderItem.objects.get_or_create(order=order, product=product)
    return JsonResponse("Item was added", safe= False)
