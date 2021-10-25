from django.db import models

# Create your models here.

class Images(models.Model):
    imgId = models.AutoField(primary_key=True)
    imgName = models.CharField(max_length=500)
    imgURL = models.URLField(max_length=500)
    imgDetails = models.TextField(max_length=500)