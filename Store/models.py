from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
# main models
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products', default='uploads/products/product.png')

    # Adding Sales
    is_sale = models.BooleanField(default=False)
    sales_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.name)


class Order(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True, null=True)
    complete = models.BooleanField(default=False)
    date_ordered = models.DateField(default=datetime.datetime.today)
    transaction_id = models.CharField(max_length=100, null=True)


    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = True
        # orderitems = self.orderitem_set.all()
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(default=datetime.datetime.today)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class shippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, default='', blank=True, null=True)
    county = models.CharField(max_length=100, default='', blank=True, null=True)
    town = models.CharField(max_length=100, default='', blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    phone = models.CharField(max_length=20, default='', blank=True)
    def __str__(self):
        return self.address



# other models
class Blog(models.Model):
    thumbnail = models.ImageField(upload_to="uploads/blogs", default="uploads/blogs.blogs.jpg")
    title = models.CharField(max_length=100, blank=False, null=False)
    author = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(auto_now=True)
    content = models.TextField(blank=False, null=True, max_length=50000)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to='uploads/testimonial', default='uploads/testimonial/testimonial.jpg')
    client_name = models.CharField(blank=False, null=False, max_length=100)
    review = models.CharField(blank=False, null=False, max_length=10000)
    proffession = models.CharField(blank=False, null=True, max_length=10000)

    def __str__(self):
        return self.client_name


class Features(models.Model):
    image = models.ImageField(upload_to='uploads/features', default='uploads/features/feature.jpg')
    title = models.CharField(blank=False, null=False, max_length=100)
    description = models.CharField(blank=False, null=False, max_length=10000)

    def __str__(self):
        return self.title

class Visitors(models.Model):
        name = models.CharField(max_length=100, blank=False, null=False)
        email = models.EmailField(blank=False)
        day = models.DateField()
        phone = models.IntegerField()

        def __str__(self):
            return self.name

# model fro saving contact us messages to db

class AddMessage(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False)
    subject = models.EmailField(blank=False)
    message = models.TextField( blank=False, null=True, max_length=500)


    def __str__(self):
        return self.name

