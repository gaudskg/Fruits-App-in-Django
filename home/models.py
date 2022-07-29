from enum import unique
from operator import mod
from re import T
from tabnanny import verbose
from django.db import models
from django.forms import CharField

# Create your models here.

class fruits(models.Model):
    fruit_name = models.CharField(max_length=150)
    price = models.IntegerField()
    manufac_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    is_fresh = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.fruit_name 

    class Meta:
        db_table = 'Fruits Table'
        verbose_name = 'Fruits Table'
        ordering = ['-fruit_name']
        unique_together = [['fruit_name', 'price']]