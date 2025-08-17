"""
Middleware personalizado de seguridad para validar orígenes de solicitudes.
"""

from django.http import HttpResponseForbidden
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class SecurityOriginMiddleware:
    """
    Middleware que valida el origen de las solicitudes para mayor seguridad.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_origins = [
            'https://ispcfood.netlify.app',
            'https://www.ispcfood.netfily.app'
        ]
        
        # En modo DEBUG, permitir también localhost
        if settings.DEBUG:
            self.allowed_origins.extend([
                'http://localhost:4200',
                'http://localhost:4000',
                'http://127.0.0.1:4200',
                'http://localhost:8000',
                'http://127.0.0.1:8000',
            ])

    def __call__(self, request):
        # Obtener el origen de la solicitud
        origin = request.META.get('HTTP_ORIGIN')
        referer = request.META.get('HTTP_REFERER')
        
        # Para solicitudes AJAX/API, validar el origen
        if request.content_type == 'application/json' or '/api/' in request.path:
            if origin and origin not in self.allowed_origins:
                logger.warning(f"Solicitud bloqueada desde origen no permitido: {origin}")
                return HttpResponseForbidden("Origen no permitido")
            
            # Validar también el referer como medida adicional
            if referer and not any(referer.startswith(allowed) for allowed in self.allowed_origins):
                if not settings.DEBUG:  # Solo en producción
                    logger.warning(f"Solicitud bloqueada por referer inválido: {referer}")
                    return HttpResponseForbidden("Referer no válido")
        
        response = self.get_response(request)
        return response
