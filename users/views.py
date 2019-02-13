from django.shortcuts import render, redirect
from .forms import orderForm
from .models import order_follower, order_like
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.urls import  reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#Function for index.html
def index(request):
   return render(request, 'users/index.html')

#Class based view to make a new order
class new_order_follower(LoginRequiredMixin, CreateView):
    model = order_follower
    template_name = 'users/order.html'
    fields = ['profile_link','follower','discount','infos']
    success_url = reverse_lazy('orderhistory')
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

#class based view for order history
class order_history(LoginRequiredMixin, ListView):
    model = order_follower
    template_name = 'users/history2.html'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date')
        # validate ordering here
        return ordering

    def get_queryset(self):
        return order_follower.objects.filter(username=self.request.user)

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
