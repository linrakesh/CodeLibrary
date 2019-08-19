from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import language, code

from taggit.models import Tag

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# def home(request):
#     posts = code.objects.all()
#     return render(request, 'library/home.html', {'posts': posts})

class homeView(ListView):
    model = code
    context_object_name = 'posts'
    paginate_by = 11
    # queryset = code.objects.all().order_by('-updated_on')
    template_name = 'library/home.html'

    def get_queryset(self):
        # return code.objects.filter(author=self.request.user).order_by('-updated_on')
        if self.request.user.is_authenticated:
            return code.objects.filter(author_id=self.request.user).order_by('-updated_on')
        else:
            return code.objects.all().order_by('-updated_on')


def authorView(request, pk=None):
    posts = code.objects.all().filter(author_id__in=[pk])
    return render(request, 'library/home.html', {'posts': posts})


def tagList(request, tag_slug=None):
    posts = code.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(keywords__in=[tag])

    return render(request, 'library/home.html', {'posts': posts})


class addCode(LoginRequiredMixin, CreateView):
    model = code
    fields = ('title', 'code', 'keywords', 'language', 'updated_on', 'author')
    template_name = 'library/codeForm.html'
    success_url = reverse_lazy('home')


class updateCode(LoginRequiredMixin, UpdateView):
    model = code
    fields = ('title', 'code', 'keywords', 'language')
    context_object_name = 'post'
    template_name = 'library/codeForm.html'
    success_url = reverse_lazy('home')


class deleteCode(LoginRequiredMixin, DeleteView):
    model = code
    success_url = reverse_lazy('home')


def search_result(request):
    if request.GET:
        query = request.GET['q']
        lang = request.GET['lang']
        if lang == '':
            posts = code.objects.filter(
                keywords__name__in=[query]).order_by('-updated_on')
        else:
            posts = code.objects.filter(
                keywords__name__in=[query], language__language=lang).order_by('-updated_on')

    return render(request, 'library/home.html', {'posts': posts})


def singlecode(request, pk):
    post = code.objects.get(pk=pk)
    return render(request, "library/single.html", {'post': post})
