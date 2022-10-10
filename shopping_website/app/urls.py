from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . forms import LoginForm

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.ProductView.as_view(), name='home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html/', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.showcart, name='showcart'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('removecart/', views.remove, name='remove')
]
