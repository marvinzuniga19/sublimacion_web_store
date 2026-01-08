from .models import Cart


def cart_context(request):
    """Context processor para hacer el carrito disponible en todas las plantillas"""
    cart = None
    cart_count = 0
    
    # Asegurar que la sesión existe
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    
    try:
        cart = Cart.objects.get(session_key=session_key)
        cart_count = cart.get_total_items()
    except Cart.DoesNotExist:
        pass
    
    return {
        'cart': cart,
        'cart_count': cart_count,
    }
