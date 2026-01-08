from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.products, name='products'),
    path('producto/<slug:slug>/', views.product_detail, name='product_detail'),
    path('galeria/', views.gallery, name='gallery'),
    path('contacto/', views.contact, name='contact'),
    path('acerca/', views.about, name='about'),
    
    # Cart URLs
    path('carrito/', views.cart_view, name='cart'),
    path('carrito/agregar/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('carrito/actualizar/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('carrito/eliminar/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('carrito/count/', views.get_cart_count, name='cart_count'),
]

