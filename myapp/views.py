from django.shortcuts import render, HttpResponse
from .models import HotelsList
from django.core import serializers
from django.db.models import Q

# Create your views here.
def home(request):
  return render(request, "home.html")

# All hotels query
def hotels(request):
  hotels = HotelsList.objects.all()
  data = serializers.serialize('json', hotels)
  return HttpResponse(data, content_type='application/json')

# Hotels by city query
def filteredhotels(request):
  city_val = request.GET.get("city")
  ratings_val = request.GET.get("ratings")
  amenities_val = request.GET.get("amenities")
  
  city_data = Q()
  if (city_val != "all"):
    city_data = Q(city__icontains=city_val)
  
  ratings_data = Q(rating__gte = float(ratings_val))
  
  amenities_data = Q()
  if (amenities_val == "both"):
    amenities_data = Q(pool=True, breakfast = True)
  elif (amenities_val == "pool"):
    amenities_data = Q(pool=True)
  elif (amenities_val == "breakfast"):
    amenities_data = Q(breakfast = True)
  
  filteredhotels = HotelsList.objects.filter(city_data&ratings_data&amenities_data)
  
  data = serializers.serialize('json', filteredhotels)
  
  return HttpResponse(data, content_type='application/json')

# Request testing
def stuff(request):
  print(request.GET.get("monkey"))
  return HttpResponse("fny")