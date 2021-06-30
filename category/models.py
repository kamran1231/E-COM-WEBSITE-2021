from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=250,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)


    #change name from admin
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


