import re
from django.shortcuts import render

# Create your views here.

def random(request):
    return render(request, 'activities/random.html')
