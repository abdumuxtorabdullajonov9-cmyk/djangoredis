from django.urls import path
from .views import product_list_view, trigger_sms_view

urlpatterns = [
    path('products/', product_list_view, name='product_list'),
    path('send-sms/', trigger_sms_view, name='send_sms'),
]
