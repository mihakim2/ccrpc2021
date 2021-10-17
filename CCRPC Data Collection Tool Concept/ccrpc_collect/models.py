from djgeojson.fields import GeometryCollectionField
from django.db import models


class DataPointSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    picture = models.ImageField()
    Datatype = models.CharField(max_length=256, choices=[('Recording','Recording'), ('Observation','Observation'),('Feedback','Feedback')])
    geom =  GeometryCollectionField()

    def __str__(self):
        return self.title

    @property
    def picture_url(self):
        return self.picture.url
