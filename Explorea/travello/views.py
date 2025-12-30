from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):
    city = request.GET.get('city')
    budget = request.GET.get('budget')
    dests = Destination.objects.all()

    if city:
        dests = dests.filter(name__icontains=city)

    if budget:
        dests = dests.filter(price__lte=budget)

    return render(request, "index.html", {'dests': dests})