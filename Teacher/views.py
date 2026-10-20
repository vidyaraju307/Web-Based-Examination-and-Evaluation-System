from django.shortcuts import render

def login(request):
    if request.method=="POST":
            email=request.POST['email']
            password=request.POST['password']
            user=Registration.objects.filter(email=email,password=password).first()
            if user:
                request.session['user_id']=user.id
                messages.success(request,"Logined Successfully")
                return redirect('stddash')
            else:
                messages.error(request,"Invalid Username and Password")
        return render(request,'login.html')

