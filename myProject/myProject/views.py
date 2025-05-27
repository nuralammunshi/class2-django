from django.shortcuts import render
from myApp.models import *

def homepage(req):
    return render (req ,'index.html')

# def studenttable(req):
#     name =studentModel.objects.all()
#     context = {
#         "studentData" : name,
#     }
#     return render (req,'studenttabel.html', context)


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