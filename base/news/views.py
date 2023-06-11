from django.shortcuts import render, redirect
from .models import Fmodel
from .forms import FmodelForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
class NewsContents(DetailView):
    model = Fmodel
    template_name = 'news/content_view.html'
    context_object_name = 'news_content'

class NewsEdit(UpdateView):
    model = Fmodel
    template_name = 'news/edit_news.html'

    form_class = FmodelForm

class NewsDelete(DeleteView):
    model = Fmodel
    success_url = '/news/'
    template_name = 'news/delete_news.html'


def news_home(request):
    news = Fmodel.objects.all()

    return render(request, 'news/news_home.html', {'news': news})

def mynews_home(request):
    news = Fmodel.objects.all().filter(author=request.user)

    context = {
        'news': news
    }

    return render(request, 'news/mynews_home.html', context)

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = FmodelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news_home')
        else:
            error = 'Form filled wrong'

    form = FmodelForm

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create_news.html', data)