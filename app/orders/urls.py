from django.urls import path

from .views import OrderCreateView


add_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),

]

