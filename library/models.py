from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.


class language(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language


class code(models.Model):
    STATUS = [('Dr', 'Draft'), ('Pub', 'Published')]
    language = models.ForeignKey('language', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    code = models.TextField()
    keywords = TaggableManager()
    status = models.CharField(max_length=20, choices=STATUS, default='Dr')
    submitted_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=False)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + "-" + str(self.language)

    def get_absolute_url(self):
        return reverse('singlecode', kwargs={'pk': self.pk})


class websiteOption(models.Model):
    company_name = models.CharField(max_length=150, default="binarynote.com")
    about_us = models.TextField()
    address = models.TextField()
    phone_no = models.CharField(max_length=250)
    email = models.EmailField()
    privacy_policy = models.TextField()
    disclaimer = models.TextField()
    facebook = models.CharField(max_length=150)
    twitter = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)

    def __str__(self):
        return self.company_name + "-" + str(self.address)
