from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from Super.models import *

# Create your views here.
def login(request):
    if request.session.get('role'):
        return redirect("home")
    if request.method=="POST":
        username=request.POST.get('name')
        passwd=request.POST.get('password')
        x=tbl_register.objects.all().filter(username=username)
        x=tbl_register.objects.all().filter(username=username,password=passwd).count()
        if x==1:
            y=tbl_register.objects.all().filter(username=username)
            request.session['username']=str(y[0].username)
            request.session['name']=str(y[0].name)
            request.session['role']=str(y[0].role)
            request.session['mobile']=str(y[0].mobile)
            return HttpResponse("<script>alert('login successfully');location.href='/'</script>")
        else :
             return HttpResponse("<script>alert('username or password is incorrect');location.href='/login'</script>")
    return render(request,"viewer/login.html")


def logout(request):
    if request.session.get('username'):
        del request.session['username']
        del request.session['role']
        return HttpResponse("<script>alert('logout successfully');location.href='/'</script>")
    return redirect("home")


def register(request):
    if request.session.get('role'):
        return redirect("home")
    if request.method == "POST":
        role=request.POST.get('role')
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')  
        confirm_passwd=request.POST.get('passwdconfirm')        
        x=tbl_register.objects.all().filter(mobile=mobile).count()
        y=tbl_register.objects.all().filter(username=username).count()        
        if x==1:
            return HttpResponse("<script>alert('already Registered with this number');location.href='/register/'</script>")
        elif y==1:
            return HttpResponse("<script>alert('already Registered with this username');location.href='/register/'</script>")   
        else:
            x=(passwd==confirm_passwd)
            if x==True:
                if len(passwd)>6 and not(passwd.isalnum()):
                    tbl_register(name=name,email=email,password=passwd,mobile=mobile,username=username,role=role).save()
                    return HttpResponse("<script>alert('Thanks for register with us..');location.href='/login/'</script>")    
                else:
                    return HttpResponse("<script>alert('password have atleast 8 character and special symbols');location.href='/login'</script>")           
    return render(request,"viewer/register.html") 