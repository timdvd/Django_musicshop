from django.db import models
from django.db.models import Q
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from publishers.models import Publisher
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

CATEGORY_CHOICES = (
    ('arrival', 'Arrival'),
    ('album', 'Album'),
)

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)
    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    def all(self):
        return self.get_queryset().active()
    def search(self, query):
        lookups = Q(title__icontains=query) | Q(price__icontains=query) | Q(category__icontains=query)
        return self.get_queryset().active().filter(lookups).distinct()

''' Product Class'''
class Product(models.Model):
    title           = models.CharField('Title', max_length=30)
    short_desc      = models.CharField('Short Description', max_length=80)
    description     = models.TextField('Full Description', default='', max_length=5000)
    price           = models.DecimalField('Price', decimal_places=2, max_digits=100)
    discount_price  = models.DecimalField('Discount Price', decimal_places=2, max_digits=100, blank=True, null=False, default=0)
    image           = models.ImageField('Product Image', upload_to='prod_pics', default='')
    category        = models.CharField('Category', max_length=30, choices=CATEGORY_CHOICES)
    author          = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='Author')
    songs           = models.ManyToManyField('self', blank=True, help_text='Choose if category is album', verbose_name='Songs')
    active          = models.BooleanField('Active', default=True)
    timestamp       = models.DateTimeField('Date', auto_now_add=True)
    slug            = models.SlugField(unique=True, null=True, blank=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{} - {}'.format(self.title, self.category)

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

''' Comment Class'''
class Comment(models.Model):
    COMMENT_STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )

    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    subject         = models.CharField(max_length=50, blank=True)
    comment         = models.CharField(max_length=300, blank=True)
    rate            = models.IntegerField(default=1)
    ip              = models.CharField(max_length=20, blank=True)
    status          = models.CharField(max_length=30, default='New', choices=COMMENT_STATUS)
    timestamp       = models.DateTimeField(auto_now_add=True)
    update_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
