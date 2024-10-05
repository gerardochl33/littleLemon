from django.db import models

# Create your models here.
class booking(models.Model):
    Name = models.CharField(max_length=100)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()

    def __str__(self):
        return f"{self.Name}"

class table(models.Model):
    Title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f"{self.Title}"