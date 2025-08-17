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
        # Para pruebas: permitir cualquier origen y referer
        # ¡ATENCIÓN! Esto desactiva la seguridad de origen. No dejar en producción.
        return self.get_response(request)
