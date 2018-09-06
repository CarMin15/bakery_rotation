import datetime

from django.shortcuts import render
from .models import BakingSlot
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    baking_list = BakingSlot.objects.order_by('-date')
    context = {
        'baking_list': baking_list
    }

    return render(request, 'baking_rotation/index.jinja', context)


def details(request, item_id):
    item = BakingSlot.objects.get(pk=item_id)
    context = {
        'item': item
    }

    return render(request, 'baking_rotation/details.jinja', context)


def upcoming(request):
    item = BakingSlot.objects.filter(
        date__lt=datetime.datetime.today()
    ).order_by('date').first()
    context = {
        'item': item,
    }
    return render(request, 'baking_rotation/upcoming.jinja', context)


def votes(request):
    context = {}
    return render(request, 'baking_rotation/votes.jinja', context)


def yours(request):
    context = {}
    return render(request, 'baking_rotation/yours.jinja', context)


def create(request):
    context = {}
    return render(request, 'baking_rotation/create.jinja', context)
