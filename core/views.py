from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category, GalleryItem
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
