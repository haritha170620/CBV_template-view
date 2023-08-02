from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.
#data render by view class
class data_render(View):
    def get(self,request):
        d={'name':'haritha','age':23}
        return render (request,'data_render.html',d)
    

#fbv_insert
def fbv_insert(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD .is_valid():
            SFD.save()
            return HttpResponse('fbv_insert is done')
    return render(request,'fbv_insert.html',d)

#cbv_insert
class cbv_insert(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'cbv_insert.html',d)
    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('cbv_insert in done')

class Temp(TemplateView):
    template_name='temp.html'
        