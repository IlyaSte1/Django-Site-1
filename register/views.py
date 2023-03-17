from django.shortcuts import render
from .forms import RegisterForm


# Create your views here.
def reg(request):
    err = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            err = 'Поля заполнены неверно'

    form = RegisterForm()
    data = {
        'form': form,
        'err': err
    }
    return render(request, 'register/register.html', data)