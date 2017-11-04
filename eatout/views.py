from django.shortcuts import render
import time
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import Dinner, Restaurant
from .forms import DinnerForm, RestaurantForm

def eatout_home(request):
    din = Dinner.objects.all()
    if len(din) > 20:
        din = din[:20]
    context = {'din': din}
    return render(request, 'eatout/eatout_home.html', context)

def dinner_detail(request, d_id):
    d = Dinner.objects.get(id=d_id)
    context = {'d': d}
    return render(request, 'eatout/dinner_detail.html', context)

def add_dinner(request):
    if request.method != 'POST':
        date = time.strftime("%Y-%m-%d")
        form = DinnerForm(initial = {'date': date, 'attendance': 2, 'e_mood': 'N/A', 't_mood': 'N/A'})
    else:
        form = DinnerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eatout:eatout_home'))
    context = {'form': form}
    return render(request, 'eatout/add_dinner.html', context)

def add_rest(request):
    if request.method != 'POST':
        form = RestaurantForm()
    else:
        form = RestaurantForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eatout:eatout_home'))
    context = {'form': form}
    return render(request, 'eatout/add_rest.html', context)

def edit_dinner(request):
    pass

def edit_rest(request):
    pass
