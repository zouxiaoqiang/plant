from django.db import models


class Plant(models.Model):
    items = models.CharField(max_length=50)
    leafchars = models.ManyToManyField('Leaf', related_name='leaf')
    flowerchars = models.ManyToManyField('Flower', related_name='flower')

    def __str__(self):
        return self.items

    class Meta:
        db_table = 'items'


class Leaf(models.Model):
    chars = models.CharField(max_length=100)

    class Meta:
        db_table = 'leaf'


class Flower(models.Model):
    chars = models.CharField(max_length=100)

    class Meta:
        db_table = 'flower'
