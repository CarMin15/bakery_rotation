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

    context = {
        'items': items,
        'upcoming': upcoming,
    }

    return render(request, 'baking_rotation/index.jinja', context)


@login_required
def details(request, item_id):
    item = BakingSlot.objects.get(pk=item_id)
    item_date = item.timesince

    context = {
        'item': item,
        'item_date': item_date
    }

    return render(request, 'baking_rotation/details.jinja', context)


@login_required
def upcoming(request):
    baking_list = BakingSlot.objects.filter(
        date__gt=datetime.datetime.today()
    ).order_by('date')

    today = datetime.datetime.today()
    this_year = today.year
    this_week = today.isocalendar()[1]
    this_week_items = []
    next_week_items = []
    later_items = []
    for b in baking_list:
        year = b.date.year
        week = b.date.isocalendar()[1]
        if year == this_year and week == this_week:
            this_week_items.append(b)
        elif (
            (year == this_year and week == this_week + 1) or
            (year == this_year + 1 and week + 52 == this_week + 1)
        ):
            next_week_items.append(b)
        else:
            later_items.append(b)

    context = {
        'baking_list': baking_list,
        'next_week_items': next_week_items,
        'this_week_items': this_week_items,
        'later_items': later_items,
    }

    return render(request, 'baking_rotation/upcoming.jinja', context)


@login_required
def votes(request):
    context = {}
    return render(request, 'baking_rotation/votes.jinja', context)


@login_required
def yours(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        instance = BakingSlot.objects.get(pk=pk)
        instance.image = request.FILES['image']
        instance.save()

    context = {
        'user_baking_slots': BakingSlot.objects.filter(
            baker=request.user,
        ).order_by('-date')
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
            form.save()
            return redirect('yours')
        else:
            context['errors'] = form.errors
            context['item'] = request.POST['item']

    return render(request, 'baking_rotation/create.jinja', context)
