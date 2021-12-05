from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Person(models.Model):
    FirstName=models.CharField(max_length=60)
    LastName=models.CharField(max_length=60)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False)
    Email = models.EmailField(max_length = 254)
    passwd = models.CharField(max_length=60)
    userId=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.userId
    


