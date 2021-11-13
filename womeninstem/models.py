from django.db import models

# Create your models here.
#form
class FormData(models.Model):
    field = models.CharField(max_length=100)
    name = models.CharField(max_length=100)  
    work = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    achieve = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name + ' ' + self.field

#story
class StoryData(models.Model):
    namess = models.CharField(max_length=100)
    story = models.CharField(max_length=500)  
    achievess = models.CharField(max_length=500)
    vlink = models.CharField(max_length=500)
    contact = models.CharField(max_length=500)
    
    def __str__(self):
        return self.namess