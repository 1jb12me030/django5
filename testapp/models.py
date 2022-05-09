#from unicodedata import name
from django.db import models

# Create your models here.
class Super(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    elocation=models.CharField(max_length=100)
    def __str__(self):
        return self.ename
    
class Teacher(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)    
    def __str__(self):
        return self.ename
    
    

class Student(models.Model) :
    eno=models.IntegerField()
    
    efirst_name=models.CharField(max_length=100, null=False)   
    elast_name = models.CharField(max_length=100)
    
    esal = models.FloatField()
    ebonus = models.IntegerField(default=0)  
    
    ephone = models.IntegerField(default=0)
    ehire_date = models.DateField()
    #edept=models.ForeignKey(Department, on_delete=models.CASCADE)
    #erole=models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ename
    
