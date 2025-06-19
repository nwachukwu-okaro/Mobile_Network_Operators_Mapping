import csv
from django.http import HttpResponse
from django.contrib.gis.geos import Point
from .models import MobileTower
import os

def load_mobile_towers_from_csv(request):
    file_path = os.path.join('sites.csv')  # Replace with actual path
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                lat = float(row['Latitude'])
                lon = float(row['Longitude'])
                location = Point(lon, lat)
                MobileTower.objects.get_or_create(
                    mno=row['\ufeffMNO'],
                    code=row['Code'],
                    location=location
                )
            except Exception as e:
                print(f"Error with row {row}: {e}")
    return HttpResponse("Mobile towers loaded successfully.")




from django.shortcuts import render
from .models import MobileTower

# Define a view function in Django named 'tower_map' that handles an HTTP request
def tower_map(request):
    # Query the database to retrieve all entries from the MobileTower model.
    # This returns a QuerySet containing all mobile tower records.
    towers = MobileTower.objects.all()
    
    # Use Django's 'render' function to combine the 'tower_map.html' template
    # with a context dictionary containing the retrieved towers.
    # The result is an HTTP response with rendered HTML.
    return render(request, 'tower_map.html', {'towers': towers})

#MNO filtering

from django.shortcuts import render
from .models import MobileTower

def tower_map(request):
    towers = MobileTower.objects.all()
    
    # Get unique MNOs
    mno_list = towers.values_list('mno', flat=True).distinct()
    
    return render(request, 'tower_map.html', {
        'towers': towers,
        'mno_list': mno_list
    })

