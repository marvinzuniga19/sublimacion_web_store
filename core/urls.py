from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.products, name='products'),
    path('producto/<slug:slug>/', views.product_detail, name='product_detail'),
    path('galeria/', views.gallery, name='gallery'),
    path('contacto/', views.contact, name='contact'),
    path('acerca/', views.about, name='about'),
]
