from django.urls import path
from . import views

from .views import SignUpView
urlpatterns = [

    path('',views.index,name = 'index'),
    path('mycart/',views.mycart,name = 'mycart'),
    path('checkout/',views.checkout,name = 'checkout'),
    path('product/',views.product,name = 'product'),
    path('accounts/signup/',SignUpView,name = 'signup'),
]