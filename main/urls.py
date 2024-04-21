from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact-information/', views.contact_info, name='contact_info'),
    path('delivery-and-payment/', views.delivery_and_payment, name='delivery_and_payment'),
]
