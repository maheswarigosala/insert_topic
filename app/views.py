from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def dept(request):
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'dept.html',d)

def emp(request):
    QLEO=Emp.objects.all()
    d={'QLEO':QLEO}
    return render(request,'emp.html',d)

def salgrade(request):
    QLSO=SalGrade.objects.all()
    d={'QLSO':QLSO}
    return render(request,'salgrade.html',d)
def bonus(request):
    QLBO=Bonus.objects.all()
    d={'QLBO':QLBO}
    return render(request,'bonus.html',d)

def insert_dept(request):
    d=int(input('enter deptno'))
    dname=input('enter dname')
    loc=input('enter location')
    NDO=Dept.objects.get_or_create(deptno=d,dname=dname,location=loc)[0]
    NDO.save()
    return HttpResponse('Inserted successfully')

def insert_emp(request):
    d=int(input('enter deptno'))
    empno=int(input('enter empno'))
    en=input('enter name')
    j=input('enter job')
    s=int(input('enter sal'))
    M=int(input('enter mgr'))
    h=input('enter date')
    c=int(input('enter Comm'))
    NDO=Dept.objects.get(deptno=d)
    NEO=Emp.objects.get_or_create(deptno=NDO,empno=empno,ename=en,job=j,sal=s,MGR=M,Hiredate=h,comm=c)[0]
    NEO.save()
    return HttpResponse('Inserted successfully')

    def insert_salgrade(request):
        g=int(input('enter grade'))
        ls=int(input('enter low salary'))
        hs=int(input('enter high sal'))
        NSO=SalGrade.objects.get_or_create(grade=g,lowsal=ls,highsal=hs)[0]
        NSO.save()
        return HttpResponse('inserted successfully')