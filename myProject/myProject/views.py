from django.shortcuts import render ,redirect
from myApp.models import *

def homepage(req):
    if req.method=='POST':
        studenName =req.POST.get('studenName')
        department =req.POST.get('department')
        studentCity =req.POST.get('studentCity')
        studentAge =req.POST.get('studentAge')

        studentAdd =studentModel(
            name =studenName ,
            department =department,
            city =studentCity,
            age  =studentAge,
        )
        studentAdd.save()
        return redirect('studentList')
    return render (req ,'index.html')



def loginpage(req):
    return render (req ,'login.html')

def signinpage(req):
    return render (req ,'signin.html')
def servicepage(req):
    return render (req ,'services.html')
def aboutpage(req):
    return render (req ,'about.html')
def contactpage(req):
    return render (req ,'contact.html')
def studentTable(req):
    studentName =studentModel.objects.all()
    contTex ={
        'data' :studentName
    }
    return render (req ,'studentTable.html', contTex)