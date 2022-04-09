from django.shortcuts import render, redirect

from .forms import UserForm

# Create your views here.

def register(request):
    # form = UserForm()
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserForm(request.POST or None)

        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    else:
        form = UserForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)
