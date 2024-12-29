from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=10)
    def __str__(self):
        return str(self.deptno)
class Emp(models.Model):
    eno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    sal=models.IntegerField()
    job=models.CharField(max_length=100)
    hiredate=models.DateField(auto_now=True)
    # mgr=models.IntegerField(null=True, blank=True)
    comm=models.IntegerField(null=True, blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename