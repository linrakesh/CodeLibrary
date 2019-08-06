from django.db import models

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
    keywords = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS)
    submitted_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now=False)

    # def __str__(self):
    #     return self.title + "-" + str(self.language)