#!/usr/bin/env python
"""
Script de verificación de seguridad para el microservicio back2fa
"""
import os
import sys
import subprocess
from pathlib import Path

def check_env_file():
    """Verifica que el archivo .env existe y no esté en el repositorio"""
    print("🔍 Verificando configuración de variables de entorno...")
    
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ ERROR: Archivo .env no encontrado")
        return False
    
    # Verificar que .env está en .gitignore
    gitignore = Path(".gitignore")
    if gitignore.exists():
        content = gitignore.read_text()
        if ".env" in content:
            print("✅ Archivo .env está protegido en .gitignore")
        else:
            print("⚠️  WARNING: .env no está en .gitignore")
    
    return True

def check_secret_key():
    """Verifica que la SECRET_KEY sea segura"""
    print("🔍 Verificando SECRET_KEY...")
    
    env_file = Path(".env")
    if env_file.exists():
        content = env_file.read_text()
        if "django-insecure" in content:
            print("❌ ERROR: Usando SECRET_KEY por defecto de Django")
            return False
        else:
            print("✅ SECRET_KEY personalizada configurada")
    
    return True

def check_debug_mode():
    """Verifica que DEBUG esté en False para producción"""
    print("🔍 Verificando modo DEBUG...")
    
    env_file = Path(".env")
    if env_file.exists():
        content = env_file.read_text()
        if "DJANGO_DEBUG=False" in content:
            print("✅ Modo DEBUG desactivado")
            return True
        else:
            print("⚠️  WARNING: Modo DEBUG activado")
    
    return False

def check_dependencies():
    """Verifica que todas las dependencias de seguridad estén instaladas"""
    print("🔍 Verificando dependencias de seguridad...")
    
    security_deps = [
        'python-dotenv',
        'django-ratelimit',
        'whitenoise',
        'dj-database-url'
    ]
    
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'list'], 
                              capture_output=True, text=True)
        installed = result.stdout
        
        all_installed = True
        for dep in security_deps:
            if dep in installed:
                print(f"✅ {dep} instalado")
            else:
                print(f"❌ {dep} NO instalado")
                all_installed = False
        
        return all_installed
    except Exception as e:
        print(f"❌ Error verificando dependencias: {e}")
        return False

def run_django_check():
    """Ejecuta el comando de verificación de Django"""
    print("🔍 Ejecutando verificación de Django...")
    
    try:
        result = subprocess.run([sys.executable, 'manage.py', 'check', '--deploy'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Verificación de Django exitosa")
            return True
        else:
            print("❌ Problemas detectados por Django:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error ejecutando verificación de Django: {e}")
        return False

def main():
    """Función principal"""
    print("🛡️  VERIFICACIÓN DE SEGURIDAD - BACK2FA MICROSERVICE")
    print("=" * 50)
    
    checks = [
        check_env_file,
        check_secret_key,
        check_debug_mode,
        check_dependencies,
        run_django_check
    ]
    
    passed = 0
    total = len(checks)
    
    for check in checks:
        if check():
            passed += 1
        print()
    
    print("📊 RESUMEN DE SEGURIDAD")
    print("=" * 50)
    print(f"Verificaciones pasadas: {passed}/{total}")
    
    if passed == total:
        print("🎉 ¡Todas las verificaciones de seguridad pasaron!")
        return True
    else:
        print("⚠️  Algunas verificaciones fallaron. Revisa los errores arriba.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
