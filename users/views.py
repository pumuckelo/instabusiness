from django.shortcuts import render
from .forms import orderForm
from .models import order
from django.contrib import messages

# Create your views here.

# def home(request):
#   return render(request, 'users/home.html')

# Function to render home.html with the order form to make new orders
def neworder(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Bestllung wurde ausgefuehrt')

    else:
        form = orderForm()
    context = {
        'orders': order.objects.all()
    }
    return render(request, 'users/home.html', {'form': form}, context)

# Function to render the orderhistory.hthml, which will show all orders filtered
# by username
def orderhistory(request):
    return render(request, 'users/orderhistory.html')

# Function to render about.html
def about(request):
    return render(request, 'users/about.html')

# Function to render contact.html
def contact(request):
    return render(request, 'users/contact.html')
