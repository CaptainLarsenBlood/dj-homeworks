from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    reader = [row for row in reader]


def bus_stations(request):

    num_page = int(request.GET.get('page', 1))
    paginator = Paginator(reader, 10)
    page = paginator.get_page(num_page)

    context = {
          'bus_stations': page
    }
    return render(request, 'stations/index.html', context)
