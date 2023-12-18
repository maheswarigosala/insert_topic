from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.dname

class Emp(models.Model):
    empno=models.IntegerField(primary_key=100)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.PositiveIntegerField()
    MGR=models.PositiveIntegerField()
    Hiredate=models.DateField()
    comm=models.PositiveIntegerField()
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename

class SalGrade(models.Model):
    grade=models.IntegerField(primary_key=100)
    lowsal=models.IntegerField()
    highsal=models.IntegerField()


class Bonus(models.Model):
    bid=models.IntegerField(primary_key=True)
    bonus=models.IntegerField()

