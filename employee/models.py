from django.db import models

# Create your models here.
class employee(models.Model):
    emp_firstname = models.CharField(max_length=25)
    emp_lastname = models.CharField(max_length=25)
    emp_username = models.CharField(max_length=50)
    emp_phone_number = models.IntegerField()

    def __str__(self):
        return self.emp_username
        