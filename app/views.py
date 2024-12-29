from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
def insertEmp(request):
    eno=int(input())
    ename=input()
    sal=int(input())
    job=input()
    hiredate=input()
    comm=input()
    if comm:
        comm=int(comm)
    else:
        comm=None
    mgr=input()
    if mgr:
        mgr=int(mgr)
        mgro=Emp.objects.get(eno=mgr)
    else:
        mgr=None
    deptno=int(input())
    deptobj=Dept.objects.get(deptno=deptno)
    ETO=Emp.objects.get_or_create(eno=eno,ename=ename,sal=sal,job=job,hiredate=hiredate,comm=comm,mgr=mgro,deptno=deptobj)
    if ETO[1]:
        return HttpResponse('new emp data is created')
    else:
        return HttpResponse('already emp is existed with provided data')
def insertDept(request):
    deptno=int(input())
    dname=input()
    loc=input()
    DTO=Dept.objects.get_or_create(deptno=deptno,dname=dname,loc=loc)
    if DTO[1]:
        return HttpResponse('new data is created')
    else:
        return HttpResponse('data is already present')

def display_dept(request):
    LDO=Dept.objects.all()
    d={'LDO':LDO}
    return render(request,'dept.htm',d)

def display_emp(request):
    LEO=Emp.objects.all()
    d={'LEO':LEO}
    return render(request,'emp.htm',d)