from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=64)
    employee_id = models.CharField(max_length=64,unique=True)
    age = models.PositiveIntegerField()
    coupon = models.CharField(max_length=64)
    email = models.EmailField()
    
    class Meta:
        db_table='Table_Registration'


    
   
