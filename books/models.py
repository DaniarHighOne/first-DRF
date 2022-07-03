
from tabnanny import verbose
from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)


    def __str__(self):
        return self.title

    class Meta():
        verbose_name = ("Book")
        verbose_name_plural = ("Books")
