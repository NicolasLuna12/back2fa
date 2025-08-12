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

1. Clona el repositorio:
	```sh
	git clone https://github.com/NicolasLuna12/back2fa.git
	cd back2fa
	```
2. Instala las dependencias:
	```sh
	pip install -r requirements.txt
	```
3. Realiza las migraciones:
	```sh
	python manage.py migrate
	```
4. Inicia el servidor de desarrollo:
	```sh
	python manage.py runserver
	```

## Uso

El microservicio expone endpoints para la gestión de autenticación 2FA. Puedes consultar la documentación de la API en los archivos de la aplicación `twofa`.

Ejemplo de endpoints:
- `/api/twofa/generate/` : Genera un código 2FA para un usuario.
- `/api/twofa/validate/` : Valida el código 2FA enviado por el usuario.

## Despliegue

El proyecto incluye un `Procfile` para facilitar el despliegue en plataformas como Heroku.

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
