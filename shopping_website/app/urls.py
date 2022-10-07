from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . forms import LoginForm

app_name = 'app'

urlpatterns = [
    # path('', views.index, name='index'),
    path('home/', views.ProductView.as_view(), name='home'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/profile.html/', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]
