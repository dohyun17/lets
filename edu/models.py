from django.db import models

class Feed(models.Model):
    content = models.CharField(max_length=100)