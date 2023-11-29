from django.urls import path
from . import views
app_name = "Store"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("blogs/", views.blogs, name="blogs"),
    path("features/", views.features, name="features"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("login_user/", views.login_user, name="signin"),
    path("logout_user/", views.logout_user, name="signout"),
    path("register_user/", views.register_user, name="signup"),
    path("viewdetails/<id>", views.viewdetails, name="viewdetails"),
    path("category/<str:name>", views.category, name="category"),
    path("blogcontent/<int:id>", views.blogcontent, name="blogcontent"),
    path("featuredetail/<int:id>", views.featuredetails, name="featuredetails"),
    path('sendmessage/', views.sendmessage, name="sendmessage"),
    path('search/', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),

]