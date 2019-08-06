from django.shortcuts import render
from django.views.generic import ListView
from .models import language, code

# Create your views here.


# def home(request):
#     posts = code.objects.all()
#     return render(request, 'library/home.html', {'posts': posts})

class homeView(ListView):
    model = code
    context_object_name = 'posts'
    paginate_by = 10
    template_name = 'library/home.html'


def search_result(request):
    if request.GET:
        query = request.GET['q']
        lang = request.GET['lang']
        if lang == '':
            posts = code.objects.filter(
                keywords__icontains=query).order_by('-updated_on')
        else:
            posts = code.objects.filter(
                keywords__icontains=query, language__language=lang).order_by('-updated_on')

    return render(request, 'library/home.html', {'posts': posts})


def singlecode(request, id):
    post = code.objects.get(pk=id)
    return render(request, "library/single.html", {'post': post})
