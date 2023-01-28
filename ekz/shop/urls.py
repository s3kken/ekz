from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
                  path('', Index.as_view(), name='index'),
                  path('product_list', Products.as_view(), name='product'),
                  path('order', Order.as_view(), name='order'),
                  path('registration', RegisterUser.as_view(), name='registration'),
                  path('profile', Profile.as_view(), name='profile'),
                  path('product', DetailView.as_view(), name='product'),
                  path('login', Login.as_view(), name='login'),
              ]