from django.shortcuts import render

from django.http import JsonResponse

from .models import Activity

import random as rd

# Create your views here.

def random(request):
    return render(request, 'activities/random.html')

def random_api(request):
    activities = []
    for i in Activity.objects.all():
        activities.append({
            'id': i.id,
            'activity': i.activity,
            'type': i._type,
        })

    if request.GET['type'] != None and request.GET['type'] != 'all':
        _activities = []
        for i in activities:
            if i['type'] == request.GET['type']:
                _activities.append(i)

        return JsonResponse(rd.choice(_activities))

    if request.GET['type'] == 'all':
        print(request.GET['type'])
        return JsonResponse(rd.choice(activities))

    return JsonResponse(rd.choice(activities))