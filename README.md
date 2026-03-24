Proyecto: CRM de Gestión de Prospectos (FullStack)
Este proyecto es un sistema de gestión de clientes potenciales (Prospectos) diseñado para optimizar el flujo de ventas. Utiliza una arquitectura desacoplada con un Backend robusto en Python y un Frontend reactivo.

🚀 Tecnologías Utilizadas
Backend: Python 3.13 + Django 6.0

API: Django REST Framework (Arquitectura RESTful)

Frontend: JavaScript (Vanilla), HTML5, Tailwind CSS

Base de Datos: SQLite (Desarrollo) / Compatible con PostgreSQL

🛠️ Características Principales
Operaciones CRUD Completas: Registro, visualización y eliminación de prospectos en tiempo real sin recargar la página.

Consumo de API Asíncrono: Uso de fetch y async/await para una experiencia de usuario fluida.

Panel Administrativo: Gestión integral de datos mediante el robusto módulo de administración de Django.

Diseño Responsivo: Interfaz moderna y limpia construida con Tailwind CSS.


## 🛠️ Instalación y Configuración Local

Para ejecutar este CRM en tu entorno local, sigue estos pasos:

**Clonar el repositorio:**
   ```bash
   git clone https://github.com/migueln06/crm-ventas-django-js.git
   cd crm-ventas-django-js

   Crear un entorno virtual:

Bash
python -m venv venv

Activar el entorno virtual:

Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

Instalar las dependencias:

Bash
pip install -r requirements.txt
Configurar la base de datos:
Asegúrate de aplicar las migraciones de Django:

Bash
python manage.py migrate

Crear un usuario administrador:
python manage.py createsuperuser

Iniciar el servidor de desarrollo:

python manage.py runserver
Luego, abre http://127.0.0.1:8000/ en tu navegador.