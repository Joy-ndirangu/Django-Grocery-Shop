from django.urls import path
from . import views
app_name = "Basket"
urlpatterns = [
    path('', views.cart_summary, name="cart_summary"),
    path('addcart/', views.cart_add, name="cart_add"),
    path('deletecart/', views.cart_delete, name="cart_delete"),
    path('updatecart/', views.cart_update, name="cart_update"),

]