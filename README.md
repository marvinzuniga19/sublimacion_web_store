# Sitio Web de Sublimación

Un sitio web profesional y moderno para un negocio de sublimación, construido con Django y diseñado con CSS moderno.

## 📑 Tabla de Contenidos

- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación Local](#️-instalación-local-desarrollo)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso del Panel de Administración](#-uso-del-panel-de-administración)
- [Modelos de Datos](#-modelos-de-datos)
- [Páginas del Sitio](#-páginas-del-sitio)
- [Carrito de Compras](#-carrito-de-compras)
- [Personalización](#-personalización)
- [Despliegue en VPS](#-despliegue-en-vps)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Soporte](#-soporte)

## 🚀 Características

- **Gestión de Productos**: Sistema completo para administrar productos y categorías
- **Carrito de Compras**: Sistema de carrito basado en sesión con indicador visual
- **Galería de Trabajos**: Muestra tus proyectos realizados
- **Formulario de Contacto**: Los clientes pueden enviarte mensajes directamente
- **Panel de Administración**: Interfaz completa para gestionar todo el contenido
- **Diseño Responsive**: Optimizado para todos los dispositivos
- **Diseño Moderno**: Interfaz atractiva con animaciones y efectos premium

## 📋 Requisitos

### Desarrollo
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Producción (VPS)
- Ubuntu 20.04/22.04 LTS o Debian 11/12 (recomendado)
- Python 3.8 o superior
- PostgreSQL 12+ (recomendado) o MySQL 8+
- Nginx
- Gunicorn
- Certbot (para SSL)
- Dominio configurado apuntando al VPS

## 🛠️ Instalación Local (Desarrollo)

### Instalación Rápida

1. **Clonar o navegar al directorio del proyecto**

   ```bash
   cd /ruta/a/tu/proyecto
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
   pip install --upgrade pip
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

### Notas de Desarrollo

- El servidor de desarrollo de Django **NO es adecuado para producción**
- SQLite se usa por defecto en desarrollo
- Los archivos estáticos se sirven automáticamente en modo DEBUG
- Para producción, sigue la guía de despliegue en VPS más abajo

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
│   ├── product_detail.html # Detalle de producto
│   ├── cart.html         # Carrito de compras
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
   - **Precio**: Ejemplo: C$150.00
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

### Cart (Carrito de Compras)

- Clave de sesión única
- Fechas de creación y actualización
- Métodos para obtener total de items y precio total

### CartItem (Item del Carrito)

- Relación con carrito y producto
- Cantidad
- Fecha de agregado
- Método para calcular subtotal

## 🎯 Páginas del Sitio

- **Inicio** (`/`): Hero section, productos destacados, galería reciente
- **Productos** (`/productos/`): Catálogo completo con filtros por categoría
- **Detalle de Producto** (`/producto/<slug>/`): Información detallada del producto con opción de agregar al carrito
- **Galería** (`/galeria/`): Trabajos realizados con filtros
- **Carrito** (`/carrito/`): Gestión del carrito de compras (agregar, actualizar cantidades, eliminar items)
- **Contacto** (`/contacto/`): Formulario de contacto e información
- **Acerca de** (`/acerca/`): Información sobre el negocio

## 🛒 Carrito de Compras

El sitio incluye un sistema completo de carrito de compras con las siguientes características:

### Funcionalidades

- **Agregar productos**: Los usuarios pueden agregar productos al carrito desde la página de detalle
- **Actualizar cantidades**: Modificar la cantidad de items directamente en el carrito
- **Eliminar items**: Remover productos del carrito con un solo clic
- **Indicador visual**: Un punto indicador aparece en el icono del carrito cuando hay items agregados
- **Actualización en tiempo real**: Todas las operaciones se realizan mediante AJAX sin recargar la página
- **Basado en sesión**: El carrito se mantiene durante la sesión del usuario (no requiere autenticación)

### Indicador del Carrito

El carrito muestra un **indicador visual** (punto circular) en el icono del carrito en la barra de navegación:
- ✅ **Visible**: Cuando hay uno o más productos en el carrito
- ❌ **Oculto**: Cuando el carrito está vacío
- El indicador tiene una animación de pulso al agregar nuevos productos

### Rutas del Carrito

- `/carrito/` - Ver el carrito completo
- `/carrito/agregar/<product_id>/` - Agregar producto al carrito
- `/carrito/actualizar/<item_id>/` - Actualizar cantidad de un item
- `/carrito/eliminar/<item_id>/` - Eliminar item del carrito

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

## 🚀 Despliegue en VPS

Esta guía te ayudará a desplegar el sitio web en un VPS (Ubuntu/Debian) de forma profesional y segura.

### 📦 Paso 1: Preparar el Servidor

#### 1.1 Actualizar el sistema

```bash
sudo apt update
sudo apt upgrade -y
```

#### 1.2 Instalar dependencias del sistema

```bash
sudo apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib nginx git curl
```

#### 1.3 Crear usuario para la aplicación (opcional pero recomendado)

```bash
sudo adduser --disabled-password --gecos "" webapp
sudo usermod -aG sudo webapp
```

### 🗄️ Paso 2: Configurar PostgreSQL

#### 2.1 Crear base de datos y usuario

```bash
sudo -u postgres psql
```

Dentro de PostgreSQL:

```sql
CREATE DATABASE web_store_db;
CREATE USER web_store_user WITH PASSWORD 'tu_password_seguro_aqui';
ALTER ROLE web_store_user SET client_encoding TO 'utf8';
ALTER ROLE web_store_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE web_store_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE web_store_db TO web_store_user;
\q
```

### 📥 Paso 3: Subir el Proyecto al Servidor

#### 3.1 Clonar o subir el proyecto

```bash
# Opción 1: Si tienes el proyecto en Git
cd /home/webapp
git clone https://github.com/tu-usuario/web_store.git
cd web_store

# Opción 2: Subir archivos vía SCP/SFTP
# Usa un cliente como FileZilla o ejecuta desde tu máquina local:
# scp -r /ruta/local/web_store usuario@tu-servidor:/home/webapp/
```

#### 3.2 Crear y activar entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3.3 Instalar dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn psycopg2-binary  # Agregar Gunicorn y driver PostgreSQL
```

### ⚙️ Paso 4: Configurar Django para Producción

#### 4.1 Crear archivo de variables de entorno

```bash
nano /home/webapp/web_store/.env
```

Agregar:

```env
DEBUG=False
SECRET_KEY=tu-clave-secreta-muy-segura-generada-aqui
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DATABASE_NAME=web_store_db
DATABASE_USER=web_store_user
DATABASE_PASSWORD=tu_password_seguro_aqui
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

**⚠️ Importante**: 
- Genera una nueva SECRET_KEY segura:
  ```bash
  python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```
- Protege el archivo `.env`:
  ```bash
  chmod 600 /home/webapp/web_store/.env
  ```
- **NUNCA** subas el archivo `.env` a Git. Agrega `.env` a `.gitignore`

#### 4.2 Actualizar settings.py

Edita `web_store/settings.py` y agrega al inicio:

```python
import os
from pathlib import Path
from dotenv import load_dotenv  # Necesitarás: pip install python-dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
```

Actualiza la configuración de base de datos:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', 'web_store_db'),
        'USER': os.getenv('DATABASE_USER', 'web_store_user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}
```

Agrega al final del archivo:

```python
# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
```

**Nota**: Si no quieres usar python-dotenv, puedes definir las variables directamente en settings.py o usar variables de entorno del sistema.

#### 4.3 Ejecutar migraciones

```bash
python manage.py migrate
```

#### 4.4 Crear superusuario

```bash
python manage.py createsuperuser
```

#### 4.5 Recopilar archivos estáticos

```bash
python manage.py collectstatic --noinput
```

### 🔧 Paso 5: Configurar Gunicorn

#### 5.1 Crear archivo de servicio systemd

```bash
sudo nano /etc/systemd/system/web_store.service
```

Agregar:

```ini
[Unit]
Description=Gunicorn daemon for web_store
After=network.target

[Service]
User=webapp
Group=www-data
WorkingDirectory=/home/webapp/web_store
ExecStart=/home/webapp/web_store/venv/bin/gunicorn \
    --access-logfile - \
    --workers 3 \
    --bind unix:/home/webapp/web_store/web_store.sock \
    web_store.wsgi:application

[Install]
WantedBy=multi-user.target
```

#### 5.2 Iniciar y habilitar el servicio

```bash
sudo systemctl daemon-reload
sudo systemctl start web_store
sudo systemctl enable web_store
sudo systemctl status web_store
```

### 🌐 Paso 6: Configurar Nginx

#### 6.1 Crear configuración de Nginx

```bash
sudo nano /etc/nginx/sites-available/web_store
```

Agregar:

```nginx
server {
    listen 80;
    server_name tudominio.com www.tudominio.com;

    # Redirigir a HTTPS (después de configurar SSL)
    # return 301 https://$server_name$request_uri;

    # Temporalmente, comentar la línea anterior y usar esta configuración HTTP:
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/webapp/web_store;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    location /media/ {
        root /home/webapp/web_store;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/webapp/web_store/web_store.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### 6.2 Habilitar el sitio

```bash
sudo ln -s /etc/nginx/sites-available/web_store /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 🔒 Paso 7: Configurar SSL con Let's Encrypt

#### 7.1 Instalar Certbot

```bash
sudo apt install -y certbot python3-certbot-nginx
```

#### 7.2 Obtener certificado SSL

```bash
sudo certbot --nginx -d tudominio.com -d www.tudominio.com
```

Sigue las instrucciones. Certbot actualizará automáticamente la configuración de Nginx.

#### 7.3 Configurar renovación automática

```bash
sudo certbot renew --dry-run
```

El certificado se renovará automáticamente cada 90 días.

#### 7.4 Descomentar redirección HTTPS en Nginx

Después de obtener el certificado, edita `/etc/nginx/sites-available/web_store` y descomenta la línea de redirección:

```nginx
return 301 https://$server_name$request_uri;
```

Reinicia Nginx:

```bash
sudo systemctl restart nginx
```

### 🔐 Paso 8: Configurar Firewall

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status
```

### 📝 Paso 9: Configuraciones Adicionales

#### 9.1 Permisos de archivos

```bash
sudo chown -R webapp:www-data /home/webapp/web_store
sudo chmod -R 755 /home/webapp/web_store
sudo chmod -R 775 /home/webapp/web_store/media
```

#### 9.2 Logs

Los logs de Gunicorn se pueden ver con:

```bash
sudo journalctl -u web_store -f
```

Los logs de Nginx están en:

```bash
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

### 🔄 Paso 10: Actualizar el Proyecto

Cuando necesites actualizar el código:

```bash
cd /home/webapp/web_store
source venv/bin/activate
git pull  # Si usas Git
# O sube los nuevos archivos vía SCP/SFTP

pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart web_store
```

### ✅ Verificación

1. Visita `http://tudominio.com` (o `https://` después de SSL)
2. Verifica que el sitio carga correctamente
3. Accede al admin: `https://tudominio.com/admin`
4. Verifica que los archivos estáticos se cargan (CSS, JS)
5. Verifica que las imágenes se muestran correctamente

### 🐛 Solución de Problemas

#### El sitio no carga
- Verifica que Gunicorn está corriendo: `sudo systemctl status web_store`
- Verifica los logs: `sudo journalctl -u web_store -n 50`
- Verifica permisos de archivos

#### Error 502 Bad Gateway
- Verifica que el socket existe: `ls -la /home/webapp/web_store/web_store.sock`
- Verifica permisos del socket
- Verifica la configuración de Nginx: `sudo nginx -t`

#### Archivos estáticos no cargan
- Verifica que `collectstatic` se ejecutó correctamente
- Verifica permisos en `/home/webapp/web_store/static/`
- Verifica la configuración de Nginx para `/static/`

#### Error de base de datos
- Verifica que PostgreSQL está corriendo: `sudo systemctl status postgresql`
- Verifica credenciales en `.env`
- Verifica que la base de datos existe: `sudo -u postgres psql -l`

### 🔒 Seguridad Adicional

#### Archivo .gitignore

Asegúrate de tener un archivo `.gitignore` en la raíz del proyecto con al menos:

```
# Variables de entorno
.env
.env.local
.env.*.local

# Base de datos
db.sqlite3
*.db

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Django
*.log
local_settings.py
/media
/staticfiles

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

#### Configurar respaldos automáticos

Crea un script de respaldo:

```bash
sudo nano /home/webapp/backup.sh
```

```bash
#!/bin/bash
BACKUP_DIR="/home/webapp/backups"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR

# Respaldar base de datos
sudo -u postgres pg_dump web_store_db > $BACKUP_DIR/db_$DATE.sql

# Respaldar archivos media
tar -czf $BACKUP_DIR/media_$DATE.tar.gz /home/webapp/web_store/media/

# Eliminar respaldos más antiguos de 7 días
find $BACKUP_DIR -type f -mtime +7 -delete
```

Hacer ejecutable y programar con cron:

```bash
chmod +x /home/webapp/backup.sh
crontab -e
# Agregar: 0 2 * * * /home/webapp/backup.sh
```

#### Monitoreo básico

Instala herramientas de monitoreo:

```bash
sudo apt install -y htop iotop
```

#### Actualizaciones de seguridad

Configura actualizaciones automáticas:

```bash
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

### 📚 Recursos Adicionales

- [Documentación de Django Deployment](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [Documentación de Gunicorn](https://docs.gunicorn.org/)
- [Documentación de Nginx](https://nginx.org/en/docs/)
- [Let's Encrypt Documentation](https://letsencrypt.org/docs/)
- [Django Security Best Practices](https://docs.djangoproject.com/en/4.2/topics/security/)

## 📚 Tecnologías Utilizadas

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción recomendada)
- **Servidor WSGI**: Gunicorn (producción)
- **Servidor Web**: Nginx (producción)
- **SSL**: Let's Encrypt / Certbot
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
