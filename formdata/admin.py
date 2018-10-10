# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from formdata.models import FormData


class FormAdmin(admin.ModelAdmin):
    pass


admin.site.register(FormData, FormAdmin)
