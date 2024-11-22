from django.db import models


class Category(models.Model):
    name        = models.CharField(max_length = 100, blank = False, null = False)
    description = models.CharField(max_length = 500)
    make_in     = models.DateTimeField(auto_now_add = True)
    update_in   = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name        = models.CharField(max_length = 255, blank = False, null = False)
    description = models.CharField(max_length = 1000)
    price       = models.DecimalField(max_digits = 10, decimal_places = 2)
    qtd_stock   = models.DecimalField(max_digits = 1000, decimal_places = 0)
    category    = models.ForeignKey(Category, on_delete = models.CASCADE)
    image       = models.ImageField(upload_to = 'products/', blank = True, null = True)
    make_in     = models.DateTimeField(auto_now_add = True) 
    update_in   = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name


class Image(models.Model):
    description = models.CharField(max_length = 30)
    image       = models.ImageField(upload_to = 'products/', blank = True, null = True)

    def __str__(self):
        return self.descricao
    