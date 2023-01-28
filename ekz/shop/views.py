from msilib.schema import ListView

import generic as generic
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from ekz.shop.models import Product, User
from django.views.generic.edit import CreateView


class Index(TemplateView):
    template_name = 'index.html'

class Products(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class Login(LoginView):
    template_name = 'login.html'
    model = User
    success_url = '/'

class RegisterUser(CreateView):
    form_class = Registration
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    success_page = 'registration'

class Profile(generic.ListView):
    model = User
    template_name = 'profile.html'

class DetailView(generic.DetailView):
    model = Product
    template_name = 'product.html'

class Order(TemplateView):
    template_name = 'order.html'
