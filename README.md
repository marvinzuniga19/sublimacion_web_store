# Sitio Web de Sublimación

Un sitio web profesional y moderno para un negocio de sublimación, construido con Django y diseñado con CSS moderno.

## 🚀 Características

- **Gestión de Productos**: Sistema completo para administrar productos y categorías
- **Galería de Trabajos**: Muestra tus proyectos realizados
- **Formulario de Contacto**: Los clientes pueden enviarte mensajes directamente
- **Panel de Administración**: Interfaz completa para gestionar todo el contenido
- **Diseño Responsive**: Optimizado para todos los dispositivos
- **Diseño Moderno**: Interfaz atractiva con animaciones y efectos premium

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

1. **Clonar o navegar al directorio del proyecto**

   ```bash
   cd /home/marvin/workspace/python/web_store
   ```

2. **Crear y activar el entorno virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones**

   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario para el panel de administración**

   ```bash
   python manage.py createsuperuser
   ```

   Sigue las instrucciones para crear tu cuenta de administrador.

6. **Ejecutar el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

7. **Abrir en el navegador**
   - Sitio web: http://localhost:8000
   - Panel de administración: http://localhost:8000/admin

## 📁 Estructura del Proyecto

```
web_store/
├── core/                   # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas
│   ├── urls.py            # URLs de la app
│   ├── forms.py           # Formularios
│   └── admin.py           # Configuración del admin
├── templates/             # Plantillas HTML
│   ├── base.html         # Template base
│   ├── home.html         # Página de inicio
│   ├── products.html     # Lista de productos
│   ├── product_detail.html
│   ├── gallery.html      # Galería
│   ├── contact.html      # Contacto
│   └── about.html        # Acerca de
├── static/               # Archivos estáticos
│   ├── css/
│   │   └── style.css    # Estilos principales
│   └── js/
│       └── main.js      # JavaScript
├── media/                # Archivos subidos
│   ├── products/        # Imágenes de productos
│   └── gallery/         # Imágenes de galería
└── web_store/           # Configuración del proyecto
    ├── settings.py
    └── urls.py
```

## 🎨 Uso del Panel de Administración

### Acceso al Panel

1. **URL**: http://localhost:8000/admin
2. **Credenciales**: Usuario y contraseña del superusuario que creaste

### Añadir Contenido al Sitio

#### 1️⃣ Crear Categorías (Primero)

Las categorías organizan tus productos y trabajos de galería.

1. En el panel admin, click en **"Categorías"** → **"Añadir categoría"**
2. Completa los campos:
   - **Nombre**: Ejemplo: "Tazas", "Camisetas", "Gorras", "Termos"
   - **Descripción**: Descripción opcional de la categoría
   - El **slug** se genera automáticamente
3. Click en **"Guardar"**

#### 2️⃣ Añadir Productos

1. Click en **"Productos"** → **"Añadir producto"**
2. Completa el formulario:
   - **Nombre del producto**: Ejemplo: "Taza Personalizada 11oz"
   - **Categoría**: Selecciona una categoría (debes crearlas primero)
   - **Descripción**: Describe el producto detalladamente
   - **Precio**: Ejemplo: 150.00
   - **Imagen**: Click en **"Examinar"** y selecciona una imagen desde tu computadora
   - ✅ **Destacado**: Marca esta opción si quieres que aparezca en la página principal
   - ✅ **Disponible**: Marca para que el producto sea visible en el sitio
3. Click en **"Guardar"**

**📁 Ubicación de imágenes**: Django guarda automáticamente las imágenes en `media/products/`

#### 3️⃣ Añadir Trabajos a la Galería

1. Click en **"Galería de Trabajos"** → **"Añadir trabajo en galería"**
2. Completa el formulario:
   - **Título**: Ejemplo: "Tazas personalizadas para evento corporativo"
   - **Descripción**: (Opcional) Detalles del trabajo realizado
   - **Imagen**: Selecciona la imagen desde tu computadora
   - **Categoría**: (Opcional) Asigna una categoría
3. Click en **"Guardar"**

**📁 Ubicación de imágenes**: Django guarda automáticamente las imágenes en `media/gallery/`

#### 4️⃣ Revisar Mensajes de Contacto

1. Click en **"Mensajes de Contacto"**
2. Verás todos los mensajes enviados desde el formulario de contacto
3. Puedes marcarlos como "Leído" para organizarlos

### 💡 Consejos Importantes

- **No subas imágenes manualmente** a las carpetas `media/`. Siempre usa el panel de administración
- **Prepara tus imágenes** antes: guárdalas en tu computadora y súbelas desde el admin
- **Tamaño de imágenes recomendado**: 800x800px para productos, 1200x800px para galería
- **Formatos soportados**: JPG, PNG, WebP
- Los directorios `media/products/` y `media/gallery/` se crean automáticamente al subir la primera imagen

## 📝 Modelos de Datos

### Category (Categoría)

- Nombre y slug
- Descripción
- Fecha de creación

### Product (Producto)

- Nombre, slug y categoría
- Descripción y precio
- Imagen
- Destacado y disponibilidad
- Fechas de creación y actualización

### GalleryItem (Elemento de Galería)

- Título y descripción
- Imagen
- Categoría (opcional)
- Fecha de creación

### ContactMessage (Mensaje de Contacto)

- Nombre, email y teléfono
- Asunto y mensaje
- Estado de lectura
- Fecha de creación

## 🎯 Páginas del Sitio

- **Inicio** (`/`): Hero section, productos destacados, galería reciente
- **Productos** (`/productos/`): Catálogo completo con filtros por categoría
- **Detalle de Producto** (`/producto/<slug>/`): Información detallada del producto
- **Galería** (`/galeria/`): Trabajos realizados con filtros
- **Contacto** (`/contacto/`): Formulario de contacto e información
- **Acerca de** (`/acerca/`): Información sobre el negocio

## 🎨 Personalización

### Colores

Edita las variables CSS en `static/css/style.css`:

```css
:root {
  --primary-color: #6366f1;
  --secondary-color: #ec4899;
  --accent-color: #f59e0b;
  /* ... más colores */
}
```

### Información de Contacto

Edita `templates/base.html` y `templates/contact.html` para actualizar:

- Correo electrónico
- Teléfono
- Dirección
- Redes sociales

### Logo y Nombre

Edita `templates/base.html` para cambiar el logo y nombre del negocio.

## 🚀 Despliegue en Producción

Antes de desplegar en producción:

1. **Actualizar settings.py**:

   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['tudominio.com']
   SECRET_KEY = 'genera-una-clave-secreta-nueva'
   ```

2. **Configurar archivos estáticos**:

   ```bash
   python manage.py collectstatic
   ```

3. **Usar una base de datos de producción** (PostgreSQL, MySQL, etc.)

4. **Configurar un servidor web** (Nginx, Apache)

5. **Usar un servidor WSGI** (Gunicorn, uWSGI)

## 📚 Tecnologías Utilizadas

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción recomendada)
- **Estilos**: CSS moderno con variables y animaciones
- **Tipografía**: Google Fonts (Inter)

## 🤝 Soporte

Para cualquier duda o problema:

- Revisa la documentación de Django: https://docs.djangoproject.com/
- Consulta los comentarios en el código

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

---

**¡Disfruta de tu nuevo sitio web de sublimación!** 🎨✨
