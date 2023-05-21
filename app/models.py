from django.db import models

# Create your models here.

class Posts(models.Model):
    post = models.CharField(max_length=99999999999999)