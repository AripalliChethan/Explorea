from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Location(models.Model):
    # This links the location to a City (e.g., Mumbai)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='locations')
    place_name = models.CharField(max_length=100)
    place_img = models.ImageField(upload_to='location_pics')
    place_desc = models.TextField()

    def __str__(self):
        return self.place_name