from django.db import models

# Create your models here.


class Cityes(models.Model):
    city = models.CharField('city', max_length=100)

    def __str__(self):
        return self.city

class Meta:
    verbose_name = 'City'
    verbose_name_plural = 'Cityes'