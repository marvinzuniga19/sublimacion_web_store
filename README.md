# Sitio Web de Sublimación

Un sitio web profesional y moderno para un negocio de sublimación, construido con Django y diseñado con CSS moderno.

## 📑 Tabla de Contenidos

- [Características](#-características)
- [Requisitos](#-requisitos)
- [Configuración de Base de Datos](#-configuración-de-base-de-datos)
  - [Opción 1: SQLite (Desarrollo)](#opción-1-sqlite-desarrollo)
  - [Opción 2: PostgreSQL (Producción)](#opción-2-postgresql-producción-recomendado)
  - [Migrar de SQLite a PostgreSQL](#-migrar-de-sqlite-a-postgresql)
- [Instalación Local](#️-instalación-local-desarrollo)
- [Variables de Entorno](#-variables-de-entorno)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Uso del Panel de Administración](#-uso-del-panel-de-administración)
- [Modelos de Datos](#-modelos-de-datos)
- [Páginas del Sitio](#-páginas-del-sitio)
- [Carrito de Compras](#-carrito-de-compras)
- [Personalización](#-personalización)
- [Guía Rápida VPS](#-guía-rápida-vps)
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
- **Soporte Dual de Base de Datos**: SQLite para desarrollo, PostgreSQL para producción
- **Configuración por Variables de Entorno**: Gestión segura de credenciales y configuración

## 📋 Requisitos

### Desarrollo Local

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- **Base de datos**: SQLite (incluido con Python, no requiere instalación)

### Producción

- Python 3.8 o superior
- PostgreSQL 12 o superior (recomendado)
- Servidor web (Nginx/Apache)
- Gunicorn o uWSGI

## 🗄️ Configuración de Base de Datos

El proyecto soporta dos opciones de base de datos que puedes elegir según tus necesidades:

### Opción 1: SQLite (Desarrollo)

**✅ Configuración por defecto** - No requiere instalación ni configuración adicional.

**Ventajas:**

- ✅ Sin instalación de software adicional
- ✅ Configuración cero
- ✅ Ideal para desarrollo y pruebas
- ✅ Base de datos en un solo archivo

**Limitaciones:**

- ❌ No recomendado para producción con múltiples usuarios concurrentes
- ❌ Menor rendimiento en aplicaciones de alto tráfico

**Uso:** Simplemente no crees un archivo `.env` o déjalo sin configurar `DB_ENGINE`. El proyecto usará SQLite automáticamente.

---

### Opción 2: PostgreSQL (Producción) **[Recomendado]**

**Ventajas:**

- ✅ Excelente rendimiento y escalabilidad
- ✅ Soporte para múltiples usuarios concurrentes
- ✅ Características avanzadas de base de datos
- ✅ Recomendado para producción

#### Instalación de PostgreSQL

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**macOS:**

```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
Descarga el instalador desde [postgresql.org](https://www.postgresql.org/download/windows/)

#### Configuración de PostgreSQL

1. **Acceder a PostgreSQL:**

   ```bash
   sudo -u postgres psql
   ```

2. **Crear base de datos y usuario:**

   ```sql
   -- Crear base de datos
   CREATE DATABASE web_store_db;

   -- Crear usuario
   CREATE USER web_store_user WITH PASSWORD 'tu_password_seguro';

   -- Configurar el usuario
   ALTER ROLE web_store_user SET client_encoding TO 'utf8';
   ALTER ROLE web_store_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE web_store_user SET timezone TO 'UTC';

   -- Otorgar privilegios
   GRANT ALL PRIVILEGES ON DATABASE web_store_db TO web_store_user;

   -- Salir
   \q
   ```

3. **Configurar variables de entorno:**

   Copia el archivo de ejemplo:

   ```bash
   cp .env.example .env
   ```

   Edita `.env` con tus credenciales:

   ```env
   # Configuración de Django
   SECRET_KEY=genera-una-clave-secreta-unica-aqui
   DEBUG=False
   ALLOWED_HOSTS=tu_dominio.com,www.tu_dominio.com

   # Configuración de PostgreSQL
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=web_store_db
   DB_USER=web_store_user
   DB_PASSWORD=tu_password_seguro
   DB_HOST=localhost
   DB_PORT=5432
   ```

4. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

#### 🔄 Migrar de SQLite a PostgreSQL

Si ya tienes datos en SQLite y quieres migrarlos a PostgreSQL:

1. **Exportar datos de SQLite:**

   ```bash
   # Asegúrate de estar usando SQLite (sin archivo .env o con DB_ENGINE=sqlite3)
   python manage.py dumpdata --natural-foreign --natural-primary \
     -e contenttypes -e auth.Permission \
     --indent 2 > datadump.json
   ```

2. **Configurar PostgreSQL:**

   - Sigue los pasos de "Configuración de PostgreSQL" arriba
   - Crea tu archivo `.env` con las credenciales de PostgreSQL

3. **Ejecutar migraciones en PostgreSQL:**

   ```bash
   python manage.py migrate
   ```

4. **Importar datos:**

   ```bash
   python manage.py loaddata datadump.json
   ```

5. **Verificar:**
   ```bash
   python manage.py runserver
   # Accede a http://localhost:8000/admin y verifica tus datos
   ```

> **💡 Tip:** Guarda el archivo `datadump.json` como respaldo antes de eliminarlo.

---

### Verificar Configuración de Base de Datos

Para verificar qué base de datos está usando tu proyecto:

```bash
python manage.py shell
```

Dentro del shell de Django:

```python
from django.conf import settings
print(settings.DATABASES['default']['ENGINE'])
# Salida: 'django.db.backends.sqlite3' o 'django.db.backends.postgresql'
```

## 🌐 Guía Rápida VPS

Preliminar para desplegar en un servidor (Ubuntu/Debian) sin entrar en configuraciones extensas:

1. **Preparar el servidor**

   - Actualiza paquetes: `sudo apt update && sudo apt upgrade -y`
   - Instala dependencias base: `sudo apt install -y python3 python3-venv python3-pip nginx git`

2. **Código y entorno**

   - Clona o sube el proyecto a `/srv/web_store` (ejemplo).
   - Crea venv y activa: `python3 -m venv venv && source venv/bin/activate`
   - Instala deps: `pip install -r requirements.txt` (+ `pip install gunicorn`)

3. **Configuración básica**

   - Define variables en `.env`: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=tu_dominio`, `DATABASE_*` si usas PostgreSQL/MySQL.
   - Apunta `STATIC_ROOT` y `MEDIA_ROOT` si decides servirlos desde Nginx (`collectstatic` requerido).

4. **Migraciones y estáticos**

   - `python manage.py migrate`
   - `python manage.py collectstatic --noinput`

5. **Servicio de aplicación**

   - Arranca Gunicorn (probar): `gunicorn web_store.wsgi:application --bind 0.0.0.0:8000`
   - Luego crea un servicio systemd para Gunicorn y un bloque de servidor en Nginx que haga proxy al puerto/socket de Gunicorn.

6. **SSL y seguridad**
   - Certbot con Nginx: `sudo certbot --nginx -d tu_dominio -d www.tu_dominio`
   - Activa firewall básico: `sudo ufw allow OpenSSH && sudo ufw allow 'Nginx Full' && sudo ufw enable`

👉 Usa esta guía como lista mínima; ajusta dominios, rutas, usuarios y base de datos según tu entorno. Para más detalle, extiende cada paso con tus configuraciones específicas.

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

4. **Configurar variables de entorno**

   Copia el archivo de ejemplo y edítalo según tu configuración:

   ```bash
   cp .env.example .env
   ```

   **Opción A: Usar SQLite (por defecto, más fácil para desarrollo)**

   No necesitas hacer nada. El proyecto usará SQLite automáticamente si no configuras PostgreSQL.

   **Opción B: Usar PostgreSQL**

   Edita el archivo `.env` y configura las variables de PostgreSQL:

   ```env
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=web_store_db
   DB_USER=tu_usuario_postgres
   DB_PASSWORD=tu_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

   Luego crea la base de datos en PostgreSQL:

   ```bash
   # Acceder a PostgreSQL
   sudo -u postgres psql

   # Crear base de datos y usuario
   CREATE DATABASE web_store_db;
   CREATE USER tu_usuario_postgres WITH PASSWORD 'tu_password';
   ALTER ROLE tu_usuario_postgres SET client_encoding TO 'utf8';
   ALTER ROLE tu_usuario_postgres SET default_transaction_isolation TO 'read committed';
   ALTER ROLE tu_usuario_postgres SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE web_store_db TO tu_usuario_postgres;
   \q
   ```

5. **Ejecutar migraciones**

   ```bash
   python manage.py migrate
   ```

6. **Crear un superusuario para el panel de administración**

   ```bash
   python manage.py createsuperuser
   ```

   Sigue las instrucciones para crear tu cuenta de administrador.

7. **Ejecutar el servidor de desarrollo**

   ```bash
   python manage.py runserver
   ```

8. **Abrir en el navegador**
   - Sitio web: http://localhost:8000
   - Panel de administración: http://localhost:8000/admin

### Notas de Desarrollo

- El servidor de desarrollo de Django **NO es adecuado para producción**
- SQLite se usa por defecto si no configuras PostgreSQL
- Para producción se recomienda usar PostgreSQL

### 🔄 Migrar Datos de SQLite a PostgreSQL

Si ya tienes datos en SQLite y quieres migrarlos a PostgreSQL:

1. **Exportar datos de SQLite**

   ```bash
   python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > datadump.json
   ```

2. **Configurar PostgreSQL** en tu archivo `.env` (ver paso 4 arriba)

3. **Ejecutar migraciones en PostgreSQL**

   ```bash
   python manage.py migrate
   ```

4. **Importar datos**
   ```bash
   python manage.py loaddata datadump.json
   ```

### 📝 Variables de Entorno

El proyecto soporta las siguientes variables de entorno en el archivo `.env`:

| Variable        | Descripción                                        | Valor por defecto            | Ejemplo                         |
| --------------- | -------------------------------------------------- | ---------------------------- | ------------------------------- |
| `SECRET_KEY`    | Clave secreta de Django (¡cámbiala en producción!) | Auto-generada                | `django-insecure-abc123...`     |
| `DEBUG`         | Modo debug (`True`/`False`)                        | `True`                       | `False`                         |
| `ALLOWED_HOSTS` | Hosts permitidos (separados por coma)              | vacío                        | `ejemplo.com,www.ejemplo.com`   |
| `DB_ENGINE`     | Motor de base de datos                             | `django.db.backends.sqlite3` | `django.db.backends.postgresql` |
| `DB_NAME`       | Nombre de la base de datos                         | `web_store_db`               | `web_store_db`                  |
| `DB_USER`       | Usuario de la base de datos                        | `postgres`                   | `web_store_user`                |
| `DB_PASSWORD`   | Contraseña de la base de datos                     | vacío                        | `mi_password_seguro`            |
| `DB_HOST`       | Host de la base de datos                           | `localhost`                  | `localhost` o `db.ejemplo.com`  |
| `DB_PORT`       | Puerto de la base de datos                         | `5432`                       | `5432`                          |

#### Generar SECRET_KEY Segura

Para producción, genera una clave secreta única:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

#### Ejemplo de Archivo `.env` para Desarrollo

```env
# Desarrollo con SQLite (no necesitas configurar DB_*)
SECRET_KEY=django-insecure-solo-para-desarrollo
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### Ejemplo de Archivo `.env` para Producción

```env
# Producción con PostgreSQL
SECRET_KEY=tu-clave-secreta-super-segura-generada
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com

# PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=web_store_db
DB_USER=web_store_user
DB_PASSWORD=password_muy_seguro_aqui
DB_HOST=localhost
DB_PORT=5432
```

> **⚠️ Importante:**
>
> - Nunca compartas tu archivo `.env` en repositorios públicos
> - El archivo `.env` está incluido en `.gitignore` para protegerlo
> - Usa contraseñas seguras en producción
> - Cambia `DEBUG=False` en producción

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

## 📚 Tecnologías Utilizadas

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Base de Datos**:
  - SQLite (desarrollo)
  - PostgreSQL (producción, soportado)
- **Adaptador de Base de Datos**: psycopg2-binary (PostgreSQL)
- **Gestión de Configuración**: python-dotenv
- **Estilos**: CSS moderno con variables y animaciones
- **Tipografía**: Google Fonts (Inter)
- **Procesamiento de Imágenes**: Pillow

## 🔧 Solución de Problemas

### Error: "No module named 'psycopg2'"

**Problema:** Django no puede encontrar el adaptador de PostgreSQL.

**Solución:**

```bash
pip install psycopg2-binary
```

### Error: "FATAL: password authentication failed"

**Problema:** Credenciales incorrectas de PostgreSQL.

**Solución:**

1. Verifica que las credenciales en `.env` sean correctas
2. Verifica que el usuario tenga permisos en la base de datos:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE web_store_db TO web_store_user;
   ```

### Error: "could not connect to server"

**Problema:** PostgreSQL no está ejecutándose o no es accesible.

**Solución:**

```bash
# Ubuntu/Debian
sudo systemctl status postgresql
sudo systemctl start postgresql

# macOS
brew services start postgresql
```

### Error: "relation does not exist"

**Problema:** Las tablas de la base de datos no existen.

**Solución:**

```bash
python manage.py migrate
```

### El proyecto no carga las variables de entorno

**Problema:** El archivo `.env` no se está leyendo.

**Solución:**

1. Verifica que el archivo se llame exactamente `.env` (no `.env.txt`)
2. Verifica que esté en el directorio raíz del proyecto
3. Verifica que `python-dotenv` esté instalado:
   ```bash
   pip install python-dotenv
   ```

### Verificar qué base de datos está usando

```bash
python manage.py shell
```

Dentro del shell:

```python
from django.conf import settings
print("Motor de BD:", settings.DATABASES['default']['ENGINE'])
print("Nombre de BD:", settings.DATABASES['default']['NAME'])
```

### Resetear la base de datos (CUIDADO: Borra todos los datos)

**SQLite:**

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

**PostgreSQL:**

```bash
sudo -u postgres psql
DROP DATABASE web_store_db;
CREATE DATABASE web_store_db;
GRANT ALL PRIVILEGES ON DATABASE web_store_db TO web_store_user;
\q

python manage.py migrate
python manage.py createsuperuser
```

## 🤝 Soporte

Para cualquier duda o problema:

- Revisa la documentación de Django: https://docs.djangoproject.com/
- Consulta los comentarios en el código

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal y comercial.

---

**¡Disfruta de tu nuevo sitio web de sublimación!** 🎨✨
