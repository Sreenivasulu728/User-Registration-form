from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def register(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            nsuo=ufd.save(commit=False)
            nsuo.set_password(ufd.cleaned_data['password'])
            nsuo.save()
            nspo=pfd.save(commit=False)
            nspo.username=nsuo
            nspo.save()
            return HttpResponse('Registration Successfull')
        else:
            return HttpResponse('invalid data')

    return render(request,'register.html',d)