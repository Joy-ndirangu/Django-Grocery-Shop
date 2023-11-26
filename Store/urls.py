from django.urls import path
from . import views
app_name = "Store"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products, name="products"),
    path("blogs/", views.products, name="blogs"),
    path("features/", views.features, name="features"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("login_user/", views.login_user, name="signin"),
    path("logout_user/", views.logout_user, name="signout"),
    path("register_user/", views.register_user, name="signup"),
    path("viewdetails/<id>", views.viewdetails, name="viewdetails"),
    path("category/<str:name>", views.category, name="category"),

]