from django.shortcuts import render, redirect
from .forms import orderForm
from .models import order_follower, order_like
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.urls import  reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.conf import settings

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
    from_email = settings.EMAIL_HOST_USER

    #subject ='Neue Bestellung'
    #from_email = settings.EMAIL_HOST_USER
    #email_message = fields
    #send_mail(
    #subject, email_message, from_email, ['abdoufacebook61@gmail.com'], fail_silently=False
    #)
    def form_valid(self, form):

        form.instance.username = self.request.user
        user = form.instance.username
        from_email = settings.EMAIL_HOST_USER
        profile_link = form.instance.profile_link
        follower = form.instance.follower

        #Method to send Email to myself with order details
        message = f"Eine Bestellung von {user}, Link: {profile_link}, Follower: {follower}"
        send_mail(
        'Neue Bestellung',
        message,
        from_email,
        ['abdoufacebook61@gmail.com'],
        fail_silently=False,
        )
        return super().form_valid(form)


#class based view for order history
class order_history(LoginRequiredMixin, ListView):
    model = order_follower
    template_name = 'users/history2.html'



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

# Function to render about.html
def about(request):
    return render(request, 'users/about.html')

# Function to render contact.html
def contact(request):
    return render(request, 'users/contact.html')

class admin_panel(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = order_follower
    template_name = 'users/history2.html'
    permission_required = 'order_follower.editorders'

    def get_queryset(self):
        return order_follower.objects.all()







#@login_required
#def orderhistory(request):
# Function to render the orderhistory.hthml, which will show all orders filtered by username
 #   context = {
  #      'orders': order_follower.objects.all()
   # }
    #return render(request, 'users/orderhistory.html', context)
