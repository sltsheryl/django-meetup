from django.db import models

# Create your models here.
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="media/images")
    address = models.CharField(max_length=200)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.address} - {self.description} - {self.image.url} - {self.isFavorite}"
