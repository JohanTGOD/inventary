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
    email = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    cellphone = models.CharField(max_length=15)
    identification_type = models.ForeignKey(IdentificationType, on_delete=models.PROTECT)
    identification_number = models.IntegerField()
    def __str__(self):
        return self.first_name


class User(models.Model):
    user_name = models.CharField(max_length=45, unique= True)
    password = models.CharField(max_length=45)
    people = models.ForeignKey(People, on_delete=models.PROTECT)
    rol = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return self.user_name


class Client(models.Model):
    people = models.ForeignKey(People, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.people)
