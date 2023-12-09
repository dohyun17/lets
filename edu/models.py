from django.db import models

class Feed(models.Model):
    content = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="image/", max_length=255, null=True, blank=True)
    