from django.shortcuts import render,redirect
from django.contrib import messages
from Teacher.models import Teacher
from Student.models import Registration     
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
    teacher=Teacher.objects.all()
    student=Registration.objects.all()
    context={
         'teacher':teacher,'student':student
    }
    return render(request,'Admin/admindash.html',context)
def add_teacher(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        qualification=request.POST['qualification']
        department=request.POST['department']
        password=request.POST['password']
        if Teacher.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
        else:
            redirect('addtr')
        Teacher.objects.create(name=name,email=email,phone=phone,qualification=qualification,department=department,password=password)
        messages.success(request,"Teacher added Succesfully!")
        return redirect('addtr')
    return render(request,'Admin/add_teacher.html')
def view_teacher(request):
    teacher=Teacher.objects.all()
    return render(request,'Admin/view_teacher.html',{'teacher':teacher})
def edit_teacher(request,id):
    teacher=Teacher.objects.get(id=id)
    if request.method=='POST':
            teacher.name=request.POST['name']
            teacher.email=request.POST['email']
            teacher.phone=request.POST['phone']
            teacher.qualification=request.POST['qualification']
            teacher.department=request.POST['department']
            teacher.save()
            messages.success(request,"Teacher details edited Successfully")
            return redirect('viewtr')
    return render(request,'Admin/edit_teacher.html',{'teacher':teacher})
def delete_teacher(request,id):
    teacher=Teacher.objects.get(id=id)
    if request.method=='POST':
            teacher.delete()
            messages.success(request,"Teacher details deleted Successfully")
            return redirect('viewtr')
    return render(request,'Admin/delete_teacher.html',{'teacher':teacher})
def view_student(request):
     student=Registration.objects.all()
     return render(request,'Admin/view_student.html',{'student':student})
def edit_student(request,id):
    student=Registration.objects.get(id=id)
    if request.method=='POST':
            student.name=request.POST['name']
            student.regnumber=request.POST['regnumber']
            student.phone=request.POST['phone']
            student.email=request.POST['email']
            student.course=request.POST['course']
            student.semester=request.POST['semester']
            student.save()
            messages.success(request,"Student details edited Successfully")
            return redirect('viewstd')
    return render(request,'Admin/edit_student.html',{'student':student})
def delete_student(request,id):
    student=Registration.objects.get(id=id)
    if request.method=='POST':
            student.delete()
            messages.success(request,"Student details deleted Successfully")
            return redirect('viewstd')
    return render(request,'Admin/delete_student.html',{'student':student})