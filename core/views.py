from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Product, Category, GalleryItem, Cart, CartItem
from .forms import ContactForm


def home(request):
    """Página de inicio"""
    featured_products = Product.objects.filter(featured=True, available=True)[:6]
    recent_gallery = GalleryItem.objects.all()[:6]
    categories = Category.objects.all()
    
    context = {
        'featured_products': featured_products,
        'recent_gallery': recent_gallery,
        'categories': categories,
    }
    return render(request, 'home.html', context)


def products(request):
    """Lista de productos"""
    category_slug = request.GET.get('category')
    products_list = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = products_list.filter(category=category)
    else:
        category = None
    
    categories = Category.objects.all()
    
    context = {
        'products': products_list,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'products.html', context)


def product_detail(request, slug):
    """Detalle de producto"""
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category,
        available=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)


def gallery(request):
    """Galería de trabajos"""
    category_slug = request.GET.get('category')
    gallery_items = GalleryItem.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        gallery_items = gallery_items.filter(category=category)
    else:
        category = None
    
    categories = Category.objects.all()
    
    context = {
        'gallery_items': gallery_items,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'gallery.html', context)


def contact(request):
    """Página de contacto"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por contactarnos! Te responderemos pronto.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)


def about(request):
    """Página acerca de"""
    return render(request, 'about.html')


def get_or_create_cart(request):
    """Obtiene o crea un carrito para la sesión actual"""
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


def cart_view(request):
    """Vista del carrito de compras"""
    cart = get_or_create_cart(request)
    cart_items = cart.items.select_related('product').all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)


@require_POST
def add_to_cart(request, product_id):
    """Agregar producto al carrito"""
    try:
        product = get_object_or_404(Product, id=product_id, available=True)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity < 1:
            quantity = 1
        
        cart = get_or_create_cart(request)
        
        # Intentar obtener el item existente o crear uno nuevo
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            # Si ya existe, incrementar la cantidad
            cart_item.quantity += quantity
            cart_item.save()
        
        # Respuesta JSON para peticiones AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{product.name} agregado al carrito',
                'cart_count': cart.get_total_items(),
            })
        
        messages.success(request, f'{product.name} agregado al carrito')
        return redirect('product_detail', slug=product.slug)
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Error al agregar el producto'
            }, status=400)
        
        messages.error(request, 'Error al agregar el producto al carrito')
        return redirect('products')


@require_POST
def update_cart_item(request, item_id):
    """Actualizar cantidad de un item en el carrito"""
    try:
        cart = get_or_create_cart(request)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity < 1:
            quantity = 1
        
        cart_item.quantity = quantity
        cart_item.save()
        
        # Respuesta JSON para peticiones AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': 'Cantidad actualizada',
                'cart_count': cart.get_total_items(),
                'item_subtotal': float(cart_item.get_subtotal()),
                'cart_total': float(cart.get_total_price()),
            })
        
        messages.success(request, 'Cantidad actualizada')
        return redirect('cart')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Error al actualizar la cantidad'
            }, status=400)
        
        messages.error(request, 'Error al actualizar la cantidad')
        return redirect('cart')


@require_POST
def remove_from_cart(request, item_id):
    """Eliminar item del carrito"""
    try:
        cart = get_or_create_cart(request)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        product_name = cart_item.product.name
        cart_item.delete()
        
        # Respuesta JSON para peticiones AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{product_name} eliminado del carrito',
                'cart_count': cart.get_total_items(),
                'cart_total': float(cart.get_total_price()),
            })
        
        messages.success(request, f'{product_name} eliminado del carrito')
        return redirect('cart')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Error al eliminar el producto'
            }, status=400)
        
        messages.error(request, 'Error al eliminar el producto')
        return redirect('cart')


def get_cart_count(request):
    """Obtener el número de items en el carrito (para AJAX)"""
    cart = get_or_create_cart(request)
    return JsonResponse({
        'cart_count': cart.get_total_items(),
    })

