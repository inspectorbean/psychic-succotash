from django.shortcuts import render
import time
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import Dinner, Restaurant, Mood
from .forms import DinnerForm, RestaurantForm

try:
    if len(Mood.objects.all()) != 6:
        d = Mood.objects.all()
        d.delete()
        m = Mood(mood='N/A', value=0)
        m.save()
        m = Mood(mood=':(', value=1)
        m.save()
        m = Mood(mood=':/', value=2)
        m.save()
        m = Mood(mood=':|', value=3)
        m.save()
        m = Mood(mood=':)', value=4)
        m.save()
        m = Mood(mood=':D', value=5)
        m.save()
except:
    pass

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
        e = Mood.objects.get(value=0)
        form = DinnerForm(initial = {'date': date, 'attendance': 2, 'e_mood': e, 't_mood': e})
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
