import datetime

from django.shortcuts import render, redirect
from .models import BakingSlot
from .forms import BakingSlotForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def index(request):
    items = BakingSlot.objects.filter(
        date__lt=datetime.datetime.today()
    ).order_by('-date')

    upcoming = BakingSlot.objects.filter(
        date__gt=datetime.datetime.today()
    ).order_by('date').first()

    for item in items:
        item.pic = 'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2008/3/25/0/latin_churros.jpg.rend.hgtvcom.826.620.suffix/1383061070644.jpeg'

    context = {
        'items': items,
        'upcoming': upcoming,
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
    baking_list = BakingSlot.objects.order_by('-date')
    context = {
        'baking_list': baking_list
    }

    return render(request, 'baking_rotation/upcoming.jinja', context)


@login_required
def votes(request):
    context = {}
    return render(request, 'baking_rotation/votes.jinja', context)


@login_required
def yours(request):
    context = {
        'user_baking_slots': BakingSlot.objects.filter(
            baker=request.user,
        )
    }
    return render(request, 'baking_rotation/yours.jinja', context)


@login_required
def create(request):
    context = {
        'errors': {}
    }

    if request.method == 'POST':
        data = {
            'item': request.POST['item'],
            'date': request.POST['date'],
            'baker': request.user.id,
        }
        form = BakingSlotForm(data)

        if form.is_valid():
            print('is valid?')
            form.save()
            return redirect('yours')
        else:
            print(form.errors)
            context['errors'] = form.errors
            context['item'] = request.POST['item']

    return render(request, 'baking_rotation/create.jinja', context)
