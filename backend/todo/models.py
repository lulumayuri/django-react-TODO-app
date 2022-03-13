
from django.db import models

# Create your models here.

class Todo1(models.Model):
    title=models.CharField(max_length=200)
    desp = models.CharField(max_length=500 )
    complited = models.BooleanField(default=False)
    def __str__(self) :
        return self.title