from django.db import models

# Create your models here.
class booking(models.Model):
    Name = models.CharField(max_length=100)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()
    Tableno = models.IntegerField(default=1)
    Persons = models.IntegerField(default=1)

    def __str__(self):
        return self.Name

class table(models.Model):
    Title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return self.Title

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

class menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()

class user(models.Model):
    url = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    groups = models.CharField(max_length=100)