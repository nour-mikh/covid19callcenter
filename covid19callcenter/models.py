from django.db import models

# Create your models here.

class Caller(models.Model):
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    address = models.CharField(max_length=256)

    def __str__(self):
        return f"First name: {self.firstName}, Last Name: {self.lastName}, Age: {self.age}, Phone Number: {self.phoneNumber}, Gender: {self.gender}, Address: {self.address}"


class Patient(models.Model):
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    symptoms = models.CharField(max_length=256, default="")

    def __str__(self):
        return f"First name: {self.firstName}, Last Name: {self.lastName}, Age: {self.age}, Phone Number: {self.phoneNumber}, Gender: {self.gender}, Address: {self.address}, Symptoms: {self.symptoms}"

