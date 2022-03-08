from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=30)
    location= models.CharField(max_length=30)
    contact = models.IntegerField(null=False,default=+254)
    
    def __str__(self):
        return self.name