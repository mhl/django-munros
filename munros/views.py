# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Munro

def index(request):
    context = {
        'highest_munros': Munro.objects.filter(heightf__gte=4000).order_by('-heightf')
    }
    return render(request, 'munros/index.html', context)
