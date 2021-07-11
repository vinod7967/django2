import datetime

from django.shortcuts import render

def home(request):
    x=datetime.datetime.now()
    dic={'vinod':'python','sai':'java','uday':'c','abhi':'c++','all':{'vinod':'python','sai':'java','uday':'c','abhi':'c++'},'date':x}
    return render(request,'home.html',dic)
# Create your views here.
