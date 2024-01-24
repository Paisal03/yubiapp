from django.db import models
class Request(models.Model):
    param_a = models.IntegerField (blank=True,null=True)
    param_b = models.IntegerField (blank=True,null=True)
    param_c = models.IntegerField(blank=True,null=True)
    operator = models.CharField(max_length=20)



# Create your models here.
