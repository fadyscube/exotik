from django.shortcuts import redirect, render

from .forms import TaskForm

from .models import Task

from activities.models import Activity

import datetime

from django.http import Http404, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

import random as rd

# Create your views here.

@login_required
def index(request):
    tasks = Task.objects.filter(date=str(datetime.datetime.date(datetime.datetime.now())), user=request.user).order_by('id')

    context = {
        'tasks': tasks,
    }
    return render(request, 'todos/index.html', context)


@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            return redirect('todos:index')

        else:
            form = TaskForm()


@login_required
def remove_task(request, id):
    task = Task.objects.get(id=id)

    if task.user == request.user:
        task.delete()
        return HttpResponseRedirect(request.GET['next'])


@login_required
def calendar(request):
    tasks = Task.objects.filter(user=request.user).order_by('id')
    data = {}

    days = [str(datetime.date.today() + datetime.timedelta(days=i)) for i in range(0 - datetime.date.today().weekday(), 7 - datetime.date.today().weekday())]

    for i in days:
        data[i] = []

    for date in Task.get_dates(user=request.user):
        for task in tasks:
            if task.date == date:
                if len(data[date]) < 7:
                    data[date].append(task)
        
    context = {
        'data': data,
        'today': str(datetime.date.today()),

    }
    return render(request, 'todos/calendar.html', context)


@login_required
def old_todo(request, date):
    tasks = Task.objects.filter(date=date, user=request.user).order_by('id')
    if datetime.datetime.strptime(date, '%Y-%m-%d').date() < datetime.date.today():
        context = {
            'tasks': tasks,
            'date': date,
        }
        return render(request, 'todos/old_todo.html', context)

    else:
        if request.method == 'POST':
            form = TaskForm(request.POST)

            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.date = date
                form.save()

                return redirect('todos:old_todo', date)

        else:
            form = TaskForm()

        context = {
            'form': form,
            'date': date,
            'tasks': tasks,
        }
        return render(request, 'todos/future_todo.html', context)


@login_required
def done_task(request, id):
    task = Task.objects.get(id=id)

    if task.user == request.user:
        if task.done == False:
            task.done  = True
        else:
            task.done = False
        task.save()
        return HttpResponseRedirect(request.GET['next'])
    else:
        return Http404


@login_required
def random_calendar(request):
    activities = []
    for i in Activity.objects.all():
        activities.append({
            'id': i.id,
            'activity': i.activity,
            'type': i._type,
        })

    for date in Task.get_dates(user=request.user):
        if date >= str(datetime.date.today()):
            Task.objects.create(title=rd.choice(activities)['activity'], user=request.user, date=date, is_random=True)

    return redirect('todos:calendar')