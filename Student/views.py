from django.shortcuts import render,redirect
from .models import Registration
from Teacher.models import Teacher
from django.contrib import messages
def register(request):
    if request.POST:
        name=request.POST['name']
        regnumber=request.POST['regnumber']
        phone=request.POST['phone']
        email=request.POST['email']
        course=request.POST['course']
        semester=request.POST['semester']
        password=request.POST['password']
        user=Registration.objects.create(name=name,regnumber=regnumber,phone=phone,email=email,course=course,semester=semester,password=password)
        user.save()
        messages.success(request,"Registration Completed Successfully!")
        return redirect('login')
    return render(request,'Student/register.html')
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=Registration.objects.filter(email=email,password=password).first()
        if user:
            request.session['user_id']=user.id
            messages.success(request,"Student Logined Successfully")
            return redirect('stddash')
        else:
            messages.error(request,"Invalid Username and Password")

        teacher=Teacher.objects.filter(email=email,password=password).first()
        if teacher:
            request.session['teacher_id']=teacher.id
            messages.success(request,"Teacher Logined Successfully")
            return redirect('trdash')
        else:
            messages.error(request,"Invalid Username and Password")
            
    return render(request,'Student/login.html')
def dashboard(request):
    user_id=request.session['user_id']
    std=Registration.objects.filter(id=user_id).first()
    context={ 'std':std,}
    return render(request,'Student/dashboard.html',context)
def logout(request):
    request.session.clear()
    messages.success(request,"Logged Out Successfully")
    return redirect('login')
