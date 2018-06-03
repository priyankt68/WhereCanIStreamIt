# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import generic

class HomePage(generic.TemplateView):
    template_name = "base.html"


class Search(generic.TemplateView):
    template_name = "about.html"
