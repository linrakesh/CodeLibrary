from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import language, code, websiteOption

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
    fields = ('title', 'code', 'keywords', 'language', 'updated_on')
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


def aboutus(request):
    return render(request, "library/about.html")


def privacy(request):
    return render(request, "library/policy.html")


def disclaimer(request):
    return render(request, "library/disclaimer.html")


def write_for_us(request):
    return render(request, "library/write.html")


def submit_code(request):
    return render(request, "library/submit_code.html")


def success(request):
    return render(request, "library/success.html")


def contact_us(request):
    if request.GET:
        email_receiver = ['rakesh@binarynote.com']
        username = request.GET['user_name']
        useremail = request.GET['user_email']
        message = request.GET['message']
        message = " Sender Name :" + username + " Email ID : " + \
            useremail + " \n Message :" + message
        try:
            send_mail('Email from Code Library', message,
                      settings.EMAIL_HOST_USER, email_receiver, fail_silently=False)
        except BadHeaderError:
            return HttpResponse("Invalid Header found")
        return redirect('success')

    return render(request, "library/contact_us.html")
