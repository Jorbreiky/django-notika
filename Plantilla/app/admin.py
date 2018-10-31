from __future__ import unicode_literals

from django.contrib import admin
from .modelos.post import Post
"""
en caso de no crearse el super usuario ejecutar 'winpty python manage.py createsuperuser'

para agregar un nuevo repositorio
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Jorbreiky/django-notika.git
git push -u origin master

"""

admin.site.register(Post)