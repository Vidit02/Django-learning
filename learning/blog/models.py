from django.db import models

# Create your models here.
class Employee(models.Model):
    #do not write id
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    age = models.IntegerField()
    isActive = models.BooleanField(default = True)
    password = models.CharField(max_length = 100)
    address = models.TextField()
    salary = models.FloatField(null=True)
    mobile = models.BigIntegerField(null=True)
    createdat = models.DateTimeField(auto_now_add=True,null=True)



    #class meta to give meta information
    class Meta :
        db_table : "employee"

class Job(models.Model):
    title : models.CharField(max_length=100)
    