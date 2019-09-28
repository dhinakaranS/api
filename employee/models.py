from django.db import models

# Create your models here.
class employees(models.Model):
    emp_firstname = models.CharField(max_length=25)
    emp_lastname = models.CharField(max_length=25)
    emp_username = models.CharField(max_length=50, unique = True)
    emp_phone_number = models.IntegerField(blank = True)

    def __str__(self):
        return self.emp_username

class products(models.Model):
    product_name = models.CharField(max_length=50)
    amount = models.IntegerField()
    description = models.CharField(max_length=250)

    def __str__():
        return self.product_name

class ordered_lists(models.Model):
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    employees = models.ForeignKey(employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
