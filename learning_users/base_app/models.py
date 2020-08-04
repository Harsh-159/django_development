from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Adder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    user_pic=models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
