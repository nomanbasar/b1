from django.shortcuts import render
from django.views import View
from .models import Customer, Product,Cart, OrderPlaced
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

# Create your views here.
#def home(request):
#     return render(request, 'Shop/home.html')

class ProductView(View):
    def get(self, request):
        gentspants = Product.objects.filter(category = 'GP')
        borkhas = Product.objects.filter(category = 'BK')
        babyfashions = Product.objects.filter(category = 'BF')
        return render(request, 'Shop/home.html', {'gentspants':gentspants, 'borkhas':borkhas, 'babyfashions': babyfashions})



#def product_detail(request):
# return render(request, 'Shop/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'Shop/productdetail.html', {'product':product})


def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

# def profile(request):
# return render(request, 'Shop/profile.html')

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'Shop/profile.html', {'form':form, 'active':'btn-primary'})
    
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            division = form.cleaned_data['division']
            district = form.cleaned_data['district']
            thana = form.cleaned_data['thana']
            villorroad = form.cleaned_data['villorroad']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name, division=division,district=district, thana=thana, villorroad=villorroad, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations! Profile Updated Successfully')
        return render(request, 'Shop/profile.html', {'form':form, 'active':'btn-primary'}) 



def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'Shop/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'Shop/orders.html')

# def change_password(request):
# return render(request, 'Shop/changepassword.html')

#def lehenga(request):
# return render(request, 'Shop/lehenga.html')

def lehenga(request, data =None):
    if data == None:
        lehengas = Product.objects.filter(category = 'L')
    elif data == 'lubnan' or data == 'infinity':
        lehengas = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'below':
        lehengas = Product.objects.filter(category='L').filter(discounted_price__lt=10000)
    elif data == 'above':
        lehengas = Product.objects.filter(category='L').filter(discounted_price__gt=10000)
    return render(request, 'Shop/lehenga.html', {'lehengas':lehengas})


#def login(request):
#     return render(request, 'Shop/login.html')

#def customerregistration(request):
# return render(request, 'Shop/customerregistration.html')

class CustomerRegistrationView(View):
   def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'Shop/customerregistration.html',{'form':form})
   
   def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
           messages.success(request, 'Congratulations! Successfully Registration Done.')
           form.save()
        return render(request, 'Shop/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'Shop/checkout.html')
