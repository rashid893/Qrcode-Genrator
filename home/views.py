from django.shortcuts import render,HttpResponse
from qrcode import *
# Create your views here.
data=None
def index(request):
    
    return render(request,'index.html')
def send(request):
    global data
    if request.method =="POST":
        data=request.POST['number']
        print(data)
        img=make(data)
        img.save('static/img/test.png')
        msg="Your Qr Code Created Successfully"
        

    return render(request,'index.html',{'msg':msg,'data':data})









  




