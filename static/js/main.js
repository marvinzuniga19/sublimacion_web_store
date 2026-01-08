// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            this.classList.toggle('active');
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!event.target.closest('.nav-wrapper')) {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            }
        });
        
        // Close menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            });
        });
    }
});

// Auto-hide messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s ease-out forwards';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });
});

// Add slideOut animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add scroll animation for elements
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements with animation
document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.product-card, .feature-card, .gallery-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
        observer.observe(el);
    });
});

// Gallery lightbox functionality (simple version)
document.addEventListener('DOMContentLoaded', function() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const img = this.querySelector('img');
            const title = this.dataset.title;
            const description = this.dataset.description;
            
            // Create lightbox
            const lightbox = document.createElement('div');
            lightbox.className = 'lightbox';
            lightbox.innerHTML = `
                <div class="lightbox-content">
                    <span class="lightbox-close">&times;</span>
                    <img src="${img.src}" alt="${title}">
                    <div class="lightbox-info">
                        <h3>${title}</h3>
                        ${description ? `<p>${description}</p>` : ''}
                    </div>
                </div>
            `;
            
            document.body.appendChild(lightbox);
            document.body.style.overflow = 'hidden';
            
            // Close lightbox
            const close = lightbox.querySelector('.lightbox-close');
            close.addEventListener('click', function() {
                lightbox.remove();
                document.body.style.overflow = '';
            });
            
            lightbox.addEventListener('click', function(e) {
                if (e.target === lightbox) {
                    lightbox.remove();
                    document.body.style.overflow = '';
                }
            });
        });
    });
});

// Add lightbox styles
const lightboxStyle = document.createElement('style');
lightboxStyle.textContent = `
    .lightbox {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        animation: fadeIn 0.3s ease-out;
    }
    
    .lightbox-content {
        position: relative;
        max-width: 90%;
        max-height: 90%;
        animation: scaleIn 0.3s ease-out;
    }
    
    .lightbox-content img {
        max-width: 100%;
        max-height: 80vh;
        border-radius: 8px;
    }
    
    .lightbox-close {
        position: absolute;
        top: -40px;
        right: 0;
        font-size: 40px;
        color: white;
        cursor: pointer;
        transition: transform 0.2s;
    }
    
    .lightbox-close:hover {
        transform: scale(1.2);
    }
    
    .lightbox-info {
        color: white;
        text-align: center;
        margin-top: 20px;
    }
    
    .lightbox-info h3 {
        font-size: 24px;
        margin-bottom: 10px;
    }
    
    .lightbox-info p {
        font-size: 16px;
        opacity: 0.8;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes scaleIn {
        from {
            transform: scale(0.8);
            opacity: 0;
        }
        to {
            transform: scale(1);
            opacity: 1;
        }
    }
`;
document.head.appendChild(lightboxStyle);

// ===== CART FUNCTIONALITY =====

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Update cart badge indicator
function updateCartBadge(count) {
    const badge = document.getElementById('cartBadge');
    if (badge) {
        if (count > 0) {
            badge.classList.add('active');
            // Pulse animation
            badge.style.animation = 'none';
            setTimeout(() => {
                badge.style.animation = 'pulse 0.5s ease-out';
            }, 10);
        } else {
            badge.classList.remove('active');
        }
    }
}

// Show notification message
function showNotification(message, type = 'success') {
    const messagesContainer = document.querySelector('.messages-container') || createMessagesContainer();
    const messageDiv = document.createElement('div');
    messageDiv.className = `message message-${type}`;
    messageDiv.innerHTML = `<div class="container">${message}</div>`;
    messagesContainer.appendChild(messageDiv);
    
    setTimeout(() => {
        messageDiv.style.animation = 'slideOut 0.3s ease-out forwards';
        setTimeout(() => messageDiv.remove(), 300);
    }, 3000);
}

function createMessagesContainer() {
    const container = document.createElement('div');
    container.className = 'messages-container';
    document.body.appendChild(container);
    return container;
}

// Add to cart functionality
document.addEventListener('DOMContentLoaded', function() {
    // Handle add to cart forms (both detail and quick add)
    const addToCartForms = document.querySelectorAll('.add-to-cart-form, .quick-add-form');
    
    addToCartForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(form);
            const button = form.querySelector('button[type="submit"]');
            const btnText = button.querySelector('.btn-text');
            const btnLoading = button.querySelector('.btn-loading');
            
            // Show loading state
            if (btnText && btnLoading) {
                btnText.style.display = 'none';
                btnLoading.style.display = 'inline';
            }
            button.disabled = true;
            
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    updateCartBadge(data.cart_count);
                    showNotification(data.message, 'success');
                } else {
                    showNotification(data.message || 'Error al agregar el producto', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showNotification('Error al agregar el producto', 'error');
            })
            .finally(() => {
                // Reset button state
                if (btnText && btnLoading) {
                    btnText.style.display = 'inline';
                    btnLoading.style.display = 'none';
                }
                button.disabled = false;
            });
        });
    });
    
    // Quantity controls on product detail page
    const decreaseDetailBtn = document.querySelector('.quantity-decrease-detail');
    const increaseDetailBtn = document.querySelector('.quantity-increase-detail');
    const quantityInput = document.getElementById('quantity');
    
    if (decreaseDetailBtn && quantityInput) {
        decreaseDetailBtn.addEventListener('click', function() {
            const currentValue = parseInt(quantityInput.value) || 1;
            if (currentValue > 1) {
                quantityInput.value = currentValue - 1;
            }
        });
    }
    
    if (increaseDetailBtn && quantityInput) {
        increaseDetailBtn.addEventListener('click', function() {
            const currentValue = parseInt(quantityInput.value) || 1;
            if (currentValue < 99) {
                quantityInput.value = currentValue + 1;
            }
        });
    }
});

// Cart page functionality
document.addEventListener('DOMContentLoaded', function() {
    // Quantity controls in cart
    const decreaseBtns = document.querySelectorAll('.quantity-decrease');
    const increaseBtns = document.querySelectorAll('.quantity-increase');
    const quantityInputs = document.querySelectorAll('.cart-item .quantity-input');
    
    // Decrease quantity
    decreaseBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.dataset.itemId;
            const input = document.querySelector(`#quantity-${itemId}`);
            const currentValue = parseInt(input.value) || 1;
            
            if (currentValue > 1) {
                input.value = currentValue - 1;
                updateCartItem(itemId, currentValue - 1);
            }
        });
    });
    
    // Increase quantity
    increaseBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.dataset.itemId;
            const input = document.querySelector(`#quantity-${itemId}`);
            const currentValue = parseInt(input.value) || 1;
            
            if (currentValue < 99) {
                input.value = currentValue + 1;
                updateCartItem(itemId, currentValue + 1);
            }
        });
    });
    
    // Handle manual input change
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            const itemId = this.dataset.itemId;
            let value = parseInt(this.value) || 1;
            
            if (value < 1) value = 1;
            if (value > 99) value = 99;
            
            this.value = value;
            updateCartItem(itemId, value);
        });
    });
    
    // Remove item buttons
    const removeBtns = document.querySelectorAll('.cart-item-remove');
    removeBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.dataset.itemId;
            if (confirm('¿Estás seguro de que deseas eliminar este producto del carrito?')) {
                removeCartItem(itemId);
            }
        });
    });
});

// Update cart item quantity
function updateCartItem(itemId, quantity) {
    const formData = new FormData();
    formData.append('quantity', quantity);
    
    fetch(`/carrito/actualizar/${itemId}/`, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update subtotal for this item
            const subtotalElement = document.querySelector(`.subtotal-amount[data-item-id="${itemId}"]`);
            if (subtotalElement) {
                subtotalElement.textContent = `C$${data.item_subtotal.toFixed(2)}`;
            }
            
            // Update cart total
            const totalElement = document.getElementById('cart-total');
            const subtotalElement2 = document.getElementById('cart-subtotal');
            if (totalElement) {
                totalElement.textContent = `C$${data.cart_total.toFixed(2)}`;
            }
            if (subtotalElement2) {
                subtotalElement2.textContent = `C$${data.cart_total.toFixed(2)}`;
            }
            
            // Update badge
            updateCartBadge(data.cart_count);
        } else {
            showNotification(data.message || 'Error al actualizar la cantidad', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error al actualizar la cantidad', 'error');
    });
}

// Remove cart item
function removeCartItem(itemId) {
    const formData = new FormData();
    
    fetch(`/carrito/eliminar/${itemId}/`, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Remove the item from DOM
            const cartItem = document.querySelector(`.cart-item[data-item-id="${itemId}"]`);
            if (cartItem) {
                cartItem.style.animation = 'slideOut 0.3s ease-out forwards';
                setTimeout(() => {
                    cartItem.remove();
                    
                    // Check if cart is empty
                    const remainingItems = document.querySelectorAll('.cart-item');
                    if (remainingItems.length === 0) {
                        location.reload(); // Reload to show empty cart state
                    }
                }, 300);
            }
            
            // Update cart total
            const totalElement = document.getElementById('cart-total');
            const subtotalElement = document.getElementById('cart-subtotal');
            if (totalElement) {
                totalElement.textContent = `C$${data.cart_total.toFixed(2)}`;
            }
            if (subtotalElement) {
                subtotalElement.textContent = `C$${data.cart_total.toFixed(2)}`;
            }
            
            // Update badge
            updateCartBadge(data.cart_count);
            
            showNotification(data.message, 'success');
        } else {
            showNotification(data.message || 'Error al eliminar el producto', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error al eliminar el producto', 'error');
    });
}

// Add pulse animation for cart badge
const cartBadgeStyle = document.createElement('style');
cartBadgeStyle.textContent = `
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
`;
document.head.appendChild(cartBadgeStyle);
