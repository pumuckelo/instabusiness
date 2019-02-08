from django.shortcuts import render, redirect
from .forms import orderForm
from .models import order_follower, order_like
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
#Function for index.html
def index(request):
   return render(request, 'users/index.html')

# Function to render order.html with the order form to make new orders
@login_required
def neworder(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Bestllung wurde ausgefuehrt')

    else:
        form = orderForm()
        return render(request, 'users/order.html', {'form': form})


#Function for Register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dein Account wurde erstellt! Du kannst dich jetzt einloggen.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#Function for Login
def login(request):
    return render(request,  'users/login.html')
@login_required
def profile(request):
    return render(request, 'users/profile.html')

# Function to render the orderhistory.hthml, which will show all orders filtered by username
@login_required
def orderhistory(request):
    context = {
        'orders': order_follower.objects.all()
    }
    return render(request, 'users/orderhistory.html', context)

# Function to render about.html
def about(request):
    return render(request, 'users/about.html')

# Function to render contact.html
def contact(request):
    return render(request, 'users/contact.html')
