from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pic = models.ImageField(upload_to="user/%y/%m")
    age = models.IntegerField(default=1)
    comment = models.TextField(blank=True)
    productnum = models.TextField(blank=True)
    cardname = models.TextField(blank=True)
    cardnum = models.TextField(blank=True)
    Expiration = models.TextField(blank=True)
    CVV = models.TextField(blank=True)
    

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/user/noimage.png"
# Create your models here.
