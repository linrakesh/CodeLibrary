from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import language, code

# Create your views here.


def home(request):
    posts = code.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'library/home.html', {'posts': posts})


def singlecode(request, id):
    post = code.objects.get(pk=id)
    return render(request, "library/single.html", {'post': post})
