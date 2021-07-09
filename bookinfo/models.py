from django.db import models

# Create your models here.
class bookform(models.Model):
    bookname=models.CharField(max_length=1000, null=True)
    author=models.CharField(max_length=500, null=True)
    genre=models.CharField(max_length=100, null=True)
    language=models.CharField(max_length=100, null=True)
