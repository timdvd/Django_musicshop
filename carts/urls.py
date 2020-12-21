from django.urls import path, include
from .views import cart, cart_update, cart_delete, checkout_home, checkout_done


urlpatterns = [
    path('', cart, name='cart'),
    path('update/<slug:slug>/', cart_update, name='cart_update'),
    path('delete/<slug:slug>/', cart_delete, name='cart_delete'),
    path('checkout/', checkout_home, name='checkout'),
    path('checkout/done/', checkout_done, name='success'),
]
