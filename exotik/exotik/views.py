from django.shortcuts import render

from activities.models import Activity

import json


def index(request):
    return render(request, 'pages/index.html')
