from django.contrib import admin

from Store.models import Category, Product, Customer, Order, Blog, Features, Testimonial, Visitors, AddMessage

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Blog)
admin.site.register(Features)
admin.site.register(Testimonial)
admin.site.register(Visitors)
admin.site.register(AddMessage)