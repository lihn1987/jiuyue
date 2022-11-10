from django.db import models
from django.db import models
 
class Type1(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    def __str__(self):
        return self.name

class Detail(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    desc = models.TextField()
    index = models.BigIntegerField(blank=True, null=True)
    url = models.CharField(max_length=200,blank=True, null=True)
    type = models.ForeignKey(Type1, on_delete=models.CASCADE)
    
    

