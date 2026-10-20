from django.shortcuts import render,redirect
from django.contrib import messages
def admin_login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        if  email=="admin@gmail.com" and password=="admin123":
            request.session['admin_id']=email
            messages.success(request,"Logined Successfully")
            return redirect('admindash')
        else:
            messages.error(request,"Invalid Username and Password")
    return render(request,'Admin/adminlogin.html')
def admin_dashboard(request):
    return render(request,'Admin/admindash.html')