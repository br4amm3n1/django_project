from django.shortcuts import render
# Create your views here.
data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
    }
def index(request):
    return render(request, 'newwebpage/index.html', data)

def about(request):
    return render(request, 'newwebpage/about.html')