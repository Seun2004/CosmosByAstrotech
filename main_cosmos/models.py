from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Show(models.Model):
    #fields for the movie table
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=7000)
    year_of_Release = models.CharField(max_length=300)
    avgPlanet = models.CharField(max_length=500)
    image = models.URLField(default=None, null=True)
    
    def __str__(self):
        return self.name 
    
    def __unicode__(self):
        return self.name
    
class UserRating(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=6000)
    planet = models.CharField(max_length=600)
    
    def __str__(self):
        return self.user.username 
    
    
    