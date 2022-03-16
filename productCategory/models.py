from django.db import models
from django.urls import reverse


class Category(models.Model):
    desc = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    c_name = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.c_name
    
# Create your models here.
