from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.


class language(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language


class code(models.Model):
    STATUS = [('Dr', 'Draft'), ('Pub', 'Published')]
    language = models.ForeignKey('language', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    # code = models.TextField()
    code = HTMLField()
    keywords = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS, default='Dr')
    submitted_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=False)

    def __str__(self):
        return self.title + "-" + str(self.language)

    def get_absolute_url(self):
        return reverse('singlecode', kwargs={'pk': self.pk})
