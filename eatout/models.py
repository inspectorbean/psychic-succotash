from django.db import models

# Create your models here.

class Mood(models.Model):
    mood = models.CharField(max_length=3)

class Restaurant(models.Model):
    name = models.TextField()
    genre = models.TextField()
    address = models.TextField(blank=True, null=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    lon = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    def __str__(self):
        return self.name

class Dinner(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant)
    attendance = models.IntegerField(default = 1)
    spent = models.DecimalField(max_digits=19, decimal_places=2)
    e_mood = models.ForeignKey(Mood, related_name='emood', null=True, blank=True)
    t_mood = models.ForeignKey(Mood, related_name='tmood', null=True, blank=True)
    def __str__(self):
        return self.restaurant.name + " " + str(self.date)
