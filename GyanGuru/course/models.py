from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,null=True)
    student_data = models.CharField(max_length=255)
   
    
    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    staff_data = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name



