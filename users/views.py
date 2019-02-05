from django.shortcuts import render
from .forms import orderForm
from .models import order
from django.contrib import messages

# Create your views here.

#def home(request):
 #   return render(request, 'users/home.html')
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
