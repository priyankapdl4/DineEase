from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    date = models.DateField()

    def __str__(self):
        return self.title

class Offer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='offers/')
    discount_percentage = models.IntegerField()

    def __str__(self):
        return self.title
