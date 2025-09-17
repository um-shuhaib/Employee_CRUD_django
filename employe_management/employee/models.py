from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salery=models.IntegerField()
    designation=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=13)

    def __str__(self):
        return self.name