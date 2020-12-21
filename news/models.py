from django.db import models

# Create your models here.

class Post(models.Model):
    title       = models.CharField(max_length=30)
    short_desc  = models.CharField(max_length=100)
    text        = models.TextField()
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} -- {}'.format(self.title, self.timestamp)
