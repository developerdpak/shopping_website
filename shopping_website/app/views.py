from django.http import request
from django.shortcuts import render
from django.views import View
from .forms import CustomerRegistrationForm, CustomerProfileForm
from . models import Product
from . models import Customer
from django.contrib import messages



# Create your views here.
# def index(request):
    # return render(request, 'app/index.html')


class ProductView(View):
    def get(self, request):
        laptops = Product.objects.filter(category='L')
        television = Product.objects.filter(category='TV')
        mobiles = Product.objects.filter(category='M')
        washing_machine = Product.objects.filter(category='WM')
        return render(request, 'app/home.html', {'laptops': laptops, 'television': television, 'mobiles': mobiles, 'washing_machine': washing_machine})


class CustomerRegistration(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        print(product.id)
        return render(request, 'app/productdetail.html', {'product': product})


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form': form})

    def post(self):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulation, profile updated successfully')

        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})


def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary'})


