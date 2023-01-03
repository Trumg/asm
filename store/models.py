from django.db import models
import datetime
# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=200)
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default='',blank=True, null=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    Complete = models.BooleanField (default=False)
    image=models.ImageField(upload_to='image')
    
class Expenses(models.Model):
    activitites = models.CharField(max_length=100)
    price = models.FloatField(default='0')
    time = models.DateTimeField(default=datetime.datetime.today)
    trip = models.ForeignKey(Trip,default=0, on_delete=models.CASCADE)
    def __str__(self):
        return self.activitites
