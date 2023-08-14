from django.db import models

class mstuser(models.Model):
    srno=models.AutoField(primary_key=True)
    fnm=models.CharField(max_length=25)
    gender=models.CharField(max_length=15)
    mno=models.BigIntegerField()
    emailid=models.CharField(max_length=40)
    pwd=models.CharField(max_length=25)
    role=models.CharField(max_length=15)