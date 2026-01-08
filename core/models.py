from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """Categorías de productos de sublimación"""
    name = models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    """Productos y servicios de sublimación"""
    name = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Categoría")
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    image = models.ImageField(upload_to='products/', verbose_name="Imagen", blank=True, null=True)
    featured = models.BooleanField(default=False, verbose_name="Destacado")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    """Galería de trabajos realizados"""
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descripción")
    image = models.ImageField(upload_to='gallery/', verbose_name="Imagen")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='gallery_items', verbose_name="Categoría")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Trabajo en Galería"
        verbose_name_plural = "Galería de Trabajos"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Mensajes de contacto de clientes"""
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electrónico")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Teléfono")
    subject = models.CharField(max_length=200, verbose_name="Asunto")
    message = models.TextField(verbose_name="Mensaje")
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False, verbose_name="Leído")
    
    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class Cart(models.Model):
    """Carrito de compras basado en sesión"""
    session_key = models.CharField(max_length=40, unique=True, verbose_name="Clave de Sesión")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"Carrito {self.session_key[:8]}... ({self.get_total_items()} items)"
    
    def get_total_items(self):
        """Retorna el número total de items en el carrito"""
        return sum(item.quantity for item in self.items.all())
    
    def get_total_price(self):
        """Retorna el precio total del carrito"""
        return sum(item.get_subtotal() for item in self.items.all())


class CartItem(models.Model):
    """Item individual en el carrito de compras"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name="Carrito")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Agregado")
    
    class Meta:
        verbose_name = "Item del Carrito"
        verbose_name_plural = "Items del Carrito"
        ordering = ['-added_at']
        unique_together = ['cart', 'product']
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"
    
    def get_subtotal(self):
        """Retorna el subtotal para este item"""
        return self.product.price * self.quantity
