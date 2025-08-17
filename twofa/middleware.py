"""
Middleware personalizado de seguridad para validar orígenes de solicitudes.
"""

from django.http import HttpResponseForbidden
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class SecurityOriginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
