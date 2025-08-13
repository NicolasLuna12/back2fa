# Configuración de Variables de Entorno para Render

## Variables Requeridas

### Django Core
- `DJANGO_SECRET_KEY`: Se genera automáticamente por Render
- `DJANGO_DEBUG`: `False` (obligatorio para producción)
- `DJANGO_SECURE_SSL_REDIRECT`: `True` (para forzar HTTPS)

### Base de Datos
- `DATABASE_URL`: Se configura automáticamente por Render al crear el servicio de base de datos

### Hosts Permitidos
- `ALLOWED_HOSTS`: `tu-app-nombre.onrender.com` (reemplaza con tu dominio de Render)

### CORS (si es necesario)
- `CORS_ALLOW_ALL_ORIGINS`: `False` (recomendado para producción)

## Configuración Paso a Paso en Render

1. **Crea el Web Service**:
   - Ve a [Render Dashboard](https://dashboard.render.com)
   - Selecciona "New Web Service"
   - Conecta tu repositorio GitHub

2. **Configuración Automática**:
   - Render detectará automáticamente el `render.yaml`
   - Se creará la base de datos PostgreSQL automáticamente
   - El `DATABASE_URL` se configurará automáticamente

3. **Variables de Entorno Manuales**:
   En la sección "Environment" del dashboard de Render, agrega:
   
   ```
   DJANGO_DEBUG=False
   DJANGO_SECURE_SSL_REDIRECT=True
   ALLOWED_HOSTS=tu-app-nombre.onrender.com
   ```

4. **Deploy**:
   - Render ejecutará automáticamente el `build.sh`
   - Se ejecutarán las migraciones
   - Se recopilarán los archivos estáticos

## URLs de Ejemplo

- **Desarrollo**: `http://localhost:8000`
- **Producción**: `https://tu-app-nombre.onrender.com`

## Troubleshooting

### Error de ALLOWED_HOSTS
Si recibes un error de ALLOWED_HOSTS, asegúrate de que la variable `ALLOWED_HOSTS` incluya tu dominio de Render.

### Error de Base de Datos
Verifica que el servicio de base de datos esté ejecutándose y que `DATABASE_URL` esté configurado correctamente.

### Error de Static Files
Los archivos estáticos se recopilan automáticamente durante el build. Si hay problemas, verifica que `STATIC_ROOT` esté configurado en `settings.py`.
