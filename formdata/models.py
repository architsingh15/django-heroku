# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FormData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.first_name)
