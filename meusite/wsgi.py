# mysite/wsgi.py: um ponto de entrada para servidores da Web compatíveis com WSGI para servir ao seu projeto.

"""
WSGI config for meusite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meusite.settings')

application = get_wsgi_application()
