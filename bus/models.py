from django.db import models

# Create your models here.

class File(models.Models):
    created = models.DateTimeField(auto_now_add=True)
    path = models.TextField()

class Route(models.Model):
    agency = models.CharField(max_length=4, default="MBTA")
    route_title = models.CharField(max_length=20, blank=True, null=True)
    route_tag = models.CharField(max_length=3)
    def __str__(self):
        return self.route_tag

class Stop(models.Model):
    stop_title = models.TextField(null=True, blank=True)
    stop_tag = models.CharField(max_length=5)
    def __str__(self):
        return self.stop_title

class Prediction(models.Model):
    route = models.ForiegnKey(Route)
    stop = models.ForiegnKey(Stop)
    q_time = models.DateTimeField(auto_now_add=True)
    direction = models.TextField()
    dir_tag = models.CharField(max_length=20, null=True, blank=True)
    arr_time = models.DateTimeField(null=True, blank=True)
    arr_sec = models.IntegerField(null=True, blank=True)
    is_depart = models.NullBooleanField()
    layover = models.NullBooleanField()
    vehic = models.CharField(max_length=4, null=True, blank=True)
    trip = models.CharField(max_length=8, null=True, blank=True)
    block = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return str(self.q_time) + ' - ' + str(self.route.route_tag) + ' - ' + str(self.stop.stop_tag) + ' - ' + str(self.direction)
