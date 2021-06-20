from django.db import models


# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=250)
    des = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='poster')

    def __str__(self):
        return self.name
