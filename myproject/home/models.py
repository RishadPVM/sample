from django.db import models

# Create your models here.
class Students(models.Model):
    name =models.CharField(max_length=200)
    rollnumber=models.CharField(max_length=200)
    department=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name