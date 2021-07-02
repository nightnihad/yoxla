from django.db import models
from ckeditor.fields import RichTextField
from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class AreaCategorymodel(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images')
    class Meta:
        db_table='ərazi'
        verbose_name='ərazi'
        verbose_name_plural='ərazilər'
    def __str__(self):
        return self.name
    
class Addermodel(models.Model):
    STATUS=(
        ('DAĞLIQ','DAĞLIQ'),
        ('DÜZƏNLİK','DÜZƏNLİK'),
        ('DƏNİZQIRAĞI','DƏNİZQIRAĞI'),
        ('SƏHRA','SƏHRA')
    )
    name=models.CharField(max_length=20,null=True)
    population=models.FloatField()
    area=models.ForeignKey(AreaCategorymodel,on_delete=models.CASCADE,related_name='yazi')
    specify=models.CharField(choices=STATUS,max_length=20,default='DAĞLIQ')
    author=models.ForeignKey('customer.CustomerModel',on_delete=models.CASCADE,related_name='yazıs')
    photo=models.ImageField(upload_to='images')
    content=RichTextField()
    wdate=models.DateTimeField(auto_now_add=True)
    udate=models.DateTimeField(auto_now=True)
    class Meta:
        db_table='Yazılanlar'
        verbose_name='Yazı'
        verbose_name_plural='Yazılar'
    def __str__(self):
        return self.name

class Commentarticle(models.Model):
    entry=models.ForeignKey(Addermodel,on_delete=models.CASCADE,related_name='comment')
    content=models.TextField(max_length=2000)
    author=models.ForeignKey('customer.CustomerModel',on_delete=models.CASCADE,related_name='comments')
    wdate=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Commentlər'
        verbose_name='Comment'
        verbose_name_plural='Commentlər'
    def __str__(self):
        return str(self.entry)
        
