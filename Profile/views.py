from django.shortcuts import render,redirect
from .forms import *
from django.views import View
from django.contrib.auth import authenticate, login, logout
# Create your views here.



def logout_view(request):
    logout(request)
    return redirect('/')


class IndexView(View):
    
    def get(self,request,*args,**kwargs):
        
        return render(request,'index.html',locals())