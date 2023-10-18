from django.db import models
from user.models import Account
# Create your models here.

class Url(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    urlCount = models.IntegerField()
    url = models.CharField(max_length=1000)
    shortend_url = models.CharField(max_length=100)