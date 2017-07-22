# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post,Comment,MyProject
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(MyProject)
