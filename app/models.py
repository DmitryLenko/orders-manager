from django.db import models


# Create your models here.


class Customer(models.Model):
    products = models.ManyToManyField('Product', through='ProductOrder')


class Address(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    index = models.PositiveIntegerField()
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house = models.CharField(max_length=20)
    flat = models.PositiveIntegerField()
    floor = models.PositiveSmallIntegerField()
    entrance = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'г. {self.city}, ул. {self.street}, д. {self.house}, кв. {self.flat}'


class Phone(models.Model):
    number = models.CharField(max_length=30)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class ProductOrder(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.customer} заказал {self.number} {self.product}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    options = models.ManyToManyField('Option')
    price = models.FloatField()

    def __str__(self):
        return self.name


class Parameter(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=100)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.parameter} — {self.name}"
