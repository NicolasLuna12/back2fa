# back2fa

Este proyecto es un microservicio desarrollado en Django para la gestión de autenticación de dos factores (2FA).

## Descripción

El microservicio `back2fa` permite agregar una capa adicional de seguridad a las aplicaciones mediante la verificación en dos pasos. Está diseñado para integrarse fácilmente con otros sistemas y proveer endpoints para la gestión y validación de códigos 2FA.

## Características principales
- Generación y validación de códigos 2FA.
- Integración sencilla con otros servicios vía API REST.
- Gestión de usuarios y tokens.
- Estructura escalable y mantenible.

## Estructura del proyecto
```
back2fa/
	 ├── back2fa/         # Configuración principal de Django
	 ├── twofa/           # Aplicación para lógica de 2FA
	 ├── manage.py        # Script de administración de Django
	 ├── requirements.txt # Dependencias del proyecto
	 ├── Procfile         # Configuración para despliegue en servidores como Heroku
	 └── README.md        # Documentación
```

## Instalación

### Desarrollo Local

1. Clona el repositorio:
   ```sh
   git clone https://github.com/NicolasLuna12/back2fa.git
   cd back2fa
   ```

2. Crea un entorno virtual:
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:
   ```sh
   cp .env.example .env
   # Edita el archivo .env con tus configuraciones
   ```

5. Realiza las migraciones:
   ```sh
   python manage.py migrate
   ```

6. Inicia el servidor de desarrollo:
   ```sh
   python manage.py runserver
   ```

### Variables de Entorno

Crea un archivo `.env` basado en `.env.example` con las siguientes variables:

- `DJANGO_SECRET_KEY`: Clave secreta de Django
- `DJANGO_DEBUG`: True para desarrollo, False para producción
- `DJANGO_SECURE_SSL_REDIRECT`: True para forzar HTTPS en producción
- `DB_ENGINE`: Motor de base de datos (ej: django.db.backends.mysql)
- `DB_NAME`: Nombre de la base de datos
- `DB_USER`: Usuario de la base de datos
- `DB_PASSWORD`: Contraseña de la base de datos
- `DB_HOST`: Host de la base de datos
- `DB_PORT`: Puerto de la base de datos
- `ALLOWED_HOSTS`: Hosts permitidos separados por comas
- `CORS_ALLOW_ALL_ORIGINS`: False para producción## Uso

El microservicio expone endpoints para la gestión de autenticación 2FA. Puedes consultar la documentación de la API en los archivos de la aplicación `twofa`.

Ejemplo de endpoints:
- `/api/twofa/generate/` : Genera un código 2FA para un usuario.
- `/api/twofa/validate/` : Valida el código 2FA enviado por el usuario.

## Despliegue

### Render.com

Este proyecto está configurado para desplegarse fácilmente en Render:

1. **Fork** este repositorio en GitHub
2. Conecta tu cuenta de GitHub a [Render](https://render.com)
3. Crea un nuevo **Web Service** en Render
4. Conecta tu repositorio forkeado
5. Render detectará automáticamente la configuración desde `render.yaml`
6. Configura las siguientes variables de entorno en Render:
   - `DJANGO_SECRET_KEY`: Se genera automáticamente
   - `DJANGO_DEBUG`: False
   - `DJANGO_SECURE_SSL_REDIRECT`: True
   - `ALLOWED_HOSTS`: tu-app.onrender.com
7. Render creará automáticamente la base de datos PostgreSQL

### Variables de Entorno para Render

```env
DJANGO_DEBUG=False
DJANGO_SECURE_SSL_REDIRECT=True
ALLOWED_HOSTS=tu-app-nombre.onrender.com
```

### Otras Plataformas

El proyecto incluye configuración estándar de Django que es compatible con:
- Heroku (usando `Procfile`)
- Railway
- PythonAnywhere
- DigitalOcean App Platform

## Pruebas

Para ejecutar las pruebas:
```sh
python manage.py test twofa
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para sugerencias o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT.

## Autor

Nicolás Luna
