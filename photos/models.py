from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)


    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()


    def __str__(self):
        return self.description


class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # save location to database
    def save_location(self):
        self.save()

    # update location
    def update_location(self, name):
        self.name = name
        self.save()

     # delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name