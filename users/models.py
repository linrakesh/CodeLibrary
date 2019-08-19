from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=100, default=None)
    biodata = models.TextField(default=None)
    facebook = models.CharField(max_length=250, default=None)
    twitter = models.CharField(max_length=250, default=None)
    instagram = models.CharField(max_length=250, default=None)
    quora = models.CharField(max_length=250, default=None)
    linkedin = models.CharField(max_length=250, default=None)
    # github = models.CharField(
    #     max_length=250, default="https://github.com/linrakesh")

    profile_photo = models.ImageField(
        upload_to="profile_pics", default="default.jpg")

    def __str__(self):
        return self.profile.username + " Profile"
