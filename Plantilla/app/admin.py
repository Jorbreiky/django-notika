from __future__ import unicode_literals

from django.contrib import admin
from .modelos.user import UserDAO
"""
en caso de no crearse el super usuario ejecutar 'winpty python manage.py createsuperuser'
"""

admin.site.register(UserDAO)