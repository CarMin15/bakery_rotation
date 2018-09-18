import datetime

from django.shortcuts import render
from .models import BakingSlot
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def index(request):
    baking_list = BakingSlot.objects.order_by('-date')
    context = {
        'baking_list': baking_list
    }

    return render(request, 'baking_rotation/index.jinja', context)


@login_required
def details(request, item_id):
    item = BakingSlot.objects.get(pk=item_id)
    context = {
        'item': item
    }

    return render(request, 'baking_rotation/details.jinja', context)


@login_required
def upcoming(request):
    item = BakingSlot.objects.filter(
        date__lt=datetime.datetime.today()
    ).order_by('date').first()
    context = {
        'item': item,
    }
    return render(request, 'baking_rotation/upcoming.jinja', context)


@login_required
def votes(request):
    context = {}
    return render(request, 'baking_rotation/votes.jinja', context)


@login_required
def yours(request):
    context = {}
    return render(request, 'baking_rotation/yours.jinja', context)


@login_required
def create(request):
    if request.method == 'POST':
        print(request.POST)
        print(dir(request.POST))
        print(list(request.POST.items()))
        # BakingSlot.objects.create(
        #
        # )
        context = {}
    else:
        context = {}
    return render(request, 'baking_rotation/create.jinja', context)
