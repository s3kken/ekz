from msilib.schema import ListView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView

from .forms import Registration
from .models import Product, User
from django.views.generic.edit import CreateView


class Index(generic.ListView):
    model = Product
    template_name = 'index.html'


class Products(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class RegisterUser(generic.CreateView):
    form_class = Registration
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    success_page = 'registration'


class Profile(generic.ListView):
    model = User
    template_name = 'profile.html'


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = 'product.html'


class Order(CreateView):
    form_class = Products
    model = Product
    template_name = 'order.html'
    success_url = reverse_lazy('profile.html')
