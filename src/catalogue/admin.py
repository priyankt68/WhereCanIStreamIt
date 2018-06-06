# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Catalogue)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(Platform)