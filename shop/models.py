from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class cata(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='categery'
        verbose_name_plural='categeries'
    
    def get_url(self):
        return reverse('hh',args=[self.slug])


    def __str__(self):
        return '{}'.format(self.name)

class product(models.Model):
    name=models.CharField(max_length=300,unique=True)
    slug=models.SlugField(max_length=300,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    catagery=models.ForeignKey(cata,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('details',args=[self.catagery.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)