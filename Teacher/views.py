from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Teacher

def tr_dashboard(request):
    teacher_id=request.session.get('teacher_id')
    teacher=Teacher.objects.get(id=teacher_id)
    return render(request,'Teacher/trdashboard.html',{'teacher':teacher})

