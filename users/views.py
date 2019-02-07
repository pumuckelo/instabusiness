from django.shortcuts import render, redirect
from .forms import orderForm
from .models import order
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#Function for index.html
def index(request):
   return render(request, 'users/index.html')

# Function to render order.html with the order form to make new orders
def neworder(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Bestllung wurde ausgefuehrt')

    else:
        form = orderForm()

    return render(request, 'users/order.html', {'form': form})


#Function for Register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dein Account {username} wurde erstellt')
            return redirect('neworder')
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

#Function for Login
def login(request):
    return render(request,  'users/login.html')

# Function to render the orderhistory.hthml, which will show all orders filtered by username
def orderhistory(request):
    context = {
        'orders': order.objects.all()
    }
    return render(request, 'users/orderhistory.html', context)

# Function to render about.html
def about(request):
    return render(request, 'users/about.html')

# Function to render contact.html
def contact(request):
    return render(request, 'users/contact.html')
