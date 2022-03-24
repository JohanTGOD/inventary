from turtle import mode
from django.db import models


class Role(models.Model):
    description = models.CharField(max_length=45)

    def __str__(self):
        return self.description


class IdentificationType(models.Model):
    type = models.CharField(max_length=45)

    def __str__(self):
        return self.type


class People(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    age = models.IntegerField
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=15)
    identificatoin_number = models.IntegerField
    identification_type = models.ForeignKey(
        IdentificationType, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class User(models.Model):
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    rol = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name


class Client(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.people)
