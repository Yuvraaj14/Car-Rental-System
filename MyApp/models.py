from email.policy import default
from django.db import models

class Car(models.Model):
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30,default="")
    car_desc = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images",default="")

    def __str__(self):
        return self.car_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    cars = models.CharField(max_length=50)
    days_for_rent = models.PositiveIntegerField()
    date = models.DateField()  # or models.DateTimeField() if time is relevant
    loc_from = models.CharField(max_length=50)
    loc_to = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name
