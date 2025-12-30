from django.shortcuts import render, get_object_or_404
from .models import City, Location
from django.contrib.auth.decorators import login_required


def index(request):
    dests = City.objects.all()
    return render(request, 'index.html', {'dests': dests})

@login_required(login_url='login')
def detail(request, city_id):
    # 1. Get the city or show 404 if ID is wrong
    city = get_object_or_404(City, pk=city_id)

    # 2. FILTER: This is what stops data leaking between cities
    places = Location.objects.filter(city=city)

    return render(request, 'city_detail.html', {'city': city, 'places': places})