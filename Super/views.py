from django.shortcuts import render,redirect
from django.http import HttpResponse    
from .models import *

# Create your views here.

def admin_home(request):
    if request.session.get('role')=='Admin':
        data = post.objects.all()
        tpost= post.objects.all().count()
        tuser = tbl_register.objects.all()
        return render(request,'admin/admin_home.html',{"data" : data,"tpost":tpost,"tuser":tuser})

def admin_login(request):
    if request.session.get('role')=='Admin':
        return redirect("admin-home")
    elif request.session.get('role')=='creator' or request.session.get("role")=="Viewer":
        return redirect("home")
    elif request.method=="POST":
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('password')
        x=tbl_super.objects.all().filter(mobile=mobile)
        x=tbl_super.objects.all().filter(mobile=mobile,password=passwd).count()
        if x==1:
            print("==================================login success")
            y=tbl_super.objects.all().filter(mobile=mobile)
            request.session['name']=str(y[0].name)
            request.session['username']=str(y[0].name)
            request.session['role']="Admin"
            return redirect("admin-home")
        else :
             return HttpResponse("<script>alert('username or password is incorrect');location.href='/admin-login/'</script>")
    return render(request,"admin/admin_login.html")

def admin_logout(request):
    # if request.session.get('username'):
        print("======================","logout")
        del request.session['name']
        del request.session['role']
        # return HttpResponse("<script>alert('now you are logout');location.href='/'</script>")
        return redirect("home")
    # return redirect("home")

def admin_register(request):
    if request.session.get('role')=='Admin':
        return redirect("admin-home")
    elif request.session.get('role')=='creator' or request.session.get("role")=="Viewer":
        return redirect("home")
    elif request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')  
        confirm_passwd=request.POST.get('passwdconfirm')        
        x=tbl_super.objects.all().filter(mobile=mobile).count()       
        if x==1:
            return HttpResponse("<script>alert('already Registered with this number');location.href='/admin-register/'</script>")
        else:
            x=(passwd==confirm_passwd)
            if x==True:
                if len(passwd)>6 and not(passwd.isalnum()):
                    tbl_super(name=name,email=email,password=passwd,mobile=mobile).save()
                    return HttpResponse("<script>alert('Thanks for register with us..');location.href='/admin-login/'</script>")    
                else:
                    return HttpResponse("<script>alert('password have atleast 8 character and special symbols');location.href='/admin-login'</script>")           
    return render(request,"admin/admin_register.html") 


def add_user(request):
    if request.method == "POST":
        role=request.POST.get('role')
        username=request.POST.get('username')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')  
        x=tbl_register.objects.all().filter(mobile=mobile).count()
        y=tbl_register.objects.all().filter(username=username).count()  
        if x==1:
            return HttpResponse("<script>alert('already Registered with this number');location.href='/add-user/'</script>")
        elif y==1:
            return HttpResponse("<script>alert('already Registered with this username');location.href='/add-user/'</script>") 
        else:
            tbl_register(name=name,email=email,password=passwd,mobile=mobile,username=username,role=role).save()
            return redirect("admin-home") 
    else:
        return render(request,"admin/add_user.html")
    
    
def delete_user(request):
    if request.method=="GET":
        username=request.GET.get('username')
        tbl_register.objects.all().filter(username=username).delete()
        return redirect("admin-home")
            