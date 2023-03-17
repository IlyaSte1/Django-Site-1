from django.shortcuts import render
from news.models import News

# Create your views here.
def home_page(request):
    news = News.objects.all()

    return render(request, 'mainpage/mainpage.html', {'news': news})