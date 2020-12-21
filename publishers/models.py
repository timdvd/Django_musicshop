from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from PIL import Image
# Create your models here.

class Publisher(models.Model):
    name        = models.CharField(max_length=50, default='')
    logo        = models.ImageField(upload_to='pub_pics', default='')
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    slug            = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self):
        super().save()

        img = Image.open(self.logo.path)

        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.logo.path)

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Publisher)