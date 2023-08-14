from django.db import models

# Create your models here.
class batchbooking(models.Model):
    batchid =models.IntegerField() 
    admissionno=models.AutoField(primary_key=True)
    admissiondate=models.DateField()
    emailid=models.CharField(max_length=40)
