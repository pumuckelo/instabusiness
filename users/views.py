from django.shortcuts import render
from .forms import orderForm

# Create your views here.

def home(request):
    return render(request, 'users/home.html')
def newOrder(request):
    form = orderForm()
    return render(request, 'users/home.html', {'form': form})