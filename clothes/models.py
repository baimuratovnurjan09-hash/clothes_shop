from django.db import models

class Color(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name


class Size(models.Model):
    size_name = models.CharField(max_length=50)

    def __str__(self):
        return self.size_name



# Create your models here.
class Clothes(models.Model):
    title=models.CharField(max_length=50, verbose_name='Название товара:')
    price=models.PositiveIntegerField()
    images = models.ImageField(upload_to='images/')
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    desc = models.TextField()
    size = models.ForeignKey(Size,on_delete=models.CASCADE)




