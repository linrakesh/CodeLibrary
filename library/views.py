from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import language, code


# Create your views here.


# def home(request):
#     posts = code.objects.all()
#     return render(request, 'library/home.html', {'posts': posts})

class homeView(ListView):
    model = code
    context_object_name = 'posts'
    paginate_by = 11
    queryset = code.objects.all().order_by('-updated_on')
    template_name = 'library/home.html'

class addCode(CreateView):
    model = code
    fields = ('title','code','keywords','language','updated_on')
    template_name = 'library/codeForm.html'
    success_url = reverse_lazy('home')


class updateCode(UpdateView):
    model = code
    fields = ('title', 'code', 'keywords', 'language')
    context_object_name = 'post'
    template_name = 'library/codeForm.html'
    success_url = reverse_lazy('home')


class deleteCode(DeleteView):
    model = code
    success_url = reverse_lazy('home')

def search_result(request):
    if request.GET:
        query = request.GET['q']
        lang = request.GET['lang']
        if lang == '':
            posts = code.objects.filter(
                keywords__name__in=query).order_by('-updated_on')
        else:
            posts = code.objects.filter(
                keywords__name__in=query, language__language=lang).order_by('-updated_on')

    return render(request, 'library/home.html', {'posts': posts})


def singlecode(request, id):
    post = code.objects.get(pk=id)
    return render(request, "library/single.html", {'post': post})
