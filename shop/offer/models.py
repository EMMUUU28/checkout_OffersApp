
# Create your models here.
from django.db import models

class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Result(models.Model):
    # id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100)
    discount=models.ManyToManyField(Discount)

    def __str__(self):
        return f"Result {self.id}: {', '.join(str(discount) for discount in self.discount.all())}"
    
 
