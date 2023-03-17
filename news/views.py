from django.shortcuts import render, redirect
from .forms import NewsForm

# Create your views here.
def create_new(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    form = NewsForm()
    data = {
        'forms': form
    }
    return render(request, 'news/createnew.html', data)