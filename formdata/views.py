# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from formdata.forms import Form


class FormView(View):

    template_name = 'form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': Form()})

    def post(self, request):
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('form'))
