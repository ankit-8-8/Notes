from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.utils.timezone import localtime, now
from Super.models import *
from datetime import datetime
from django.db.models import Count

# Create your views here.

def home(request):
    user= tbl_register.objects.all().filter(mobile=request.session.get('mobile'))        
    data = post.objects.all().order_by('-pdate','-ptime')
    tpost= post.objects.all().count()
    # Get the current date in the desired timezone
    current_date = localtime(now()).date()
    daypost= post.objects.filter(pdate=current_date).count()
    if request.session.get('role')=='creator':
        return render(request,'creator/dashboard.html',{"data" : data,"tpost":tpost,"daypost":daypost,"user":user})
    if request.session.get("role")=='Admin':
        return redirect("admin-home")
    else:
        return render(request,'Viewer/home.html',{"data" : data})

def detail(request):
    if request.method=="GET":
        postid = request.GET.get("id")
        data = post.objects.all().filter(postid=postid)
        return render(request,"creator/details.html",{"data":data})
    return redirect("home")

def add(request):
    if request.session.get('username'):
        if request.method == "POST":
            username=tbl_register.objects.get(username=request.session.get("username"))
            heading = request.POST.get("heading")
            description = request.POST.get("description")
            pdf = request.FILES.get('pdf')
            image = request.FILES.get('image')
            if  image==None:
                if pdf==None:
                    post(pheading=heading,pdescription=description,pcreated_by=username).save()
                else:
                    post(pheading=heading,pdescription=description,pfile=pdf,pcreated_by=username).save()
            elif pdf==None:
                    post(pheading=heading,pdescription=description,pimage=image,pcreated_by=username).save()
            else:
                post(pheading=heading,pdescription=description,pimage=image,pfile=pdf,pcreated_by=username).save()
                
            if request.session.get('role')=='Admin':
                return redirect('admin-home')
            else:
                return HttpResponse("<script>alert('add successfully');location.href='/'</script>")
        return render(request,"creator/add.html")
    else:
        return redirect("login")

def delete(request):
    if request.method == "GET":
        postid = request.GET.get("id")
        post.objects.filter(postid=postid).delete()
    return redirect("home")


def edit(request):
        if request.method=="GET":
            postid = request.GET.get("id")
            data = post.objects.all().filter(postid=postid)
            return render(request,"creator/edit.html",{"data":data})
        elif request.method == "POST":
            postid = request.POST.get("id")
            data = post.objects.get(postid=postid)
            data.pheading = request.POST.get("heading")
            data.pdescription = request.POST.get("description")
            if request.FILES.get('pdf')==None:
                if request.FILES.get('image') ==None:
                    data.save()
                else:
                    data.pimage = request.FILES.get('image')
                    data.save()
                    # data.pfile = request.FILES.get('pdf')
            elif request.FILES.get('image')==None:
                if request.FILES.get('pdf')==None:
                    data.save()
                else:
                    data.pfile = request.FILES.get('pdf')
                    data.save()
            else:
                # data.pimage = request.FILES.get('image')
                data.save()
            if request.session.get('role')=='Admin':
                return redirect('admin-home')
            else:
                return HttpResponse("<script>alert('edit successfully');location.href='/'</script>")
            
    # return HttpResponse("<script>alert('you are not authorized to edit this post');location.href='/'</script>")

def sort(request):
    order=request.GET.get("order")
    tpost= post.objects.all().count()
    current_date = localtime(now()).date()
    daypost= post.objects.filter(pdate=current_date).count()
    if order=="desc":
        data = post.objects.all().order_by('pdate','ptime')
        print("===================================",type(data))
    elif order=="asc":
        data = post.objects.all().order_by('-pdate','-ptime')
    else:
        data = post.objects.all()
    if request.session.get('role')=='creator':
        return render(request,'creator/ss.html',{"data" : data,"tpost":tpost,"daypost":daypost})
    return render(request,'viewer/ss.html',{"data" : data})

def search(request):
        tpost= post.objects.all().count()
        current_date = localtime(now()).date()
        daypost= post.objects.filter(pdate=current_date).count()
        if request.method=="POST":
            search=request.POST.get('search')
            print("===================",search)
            data = post.objects.all().filter(pheading__icontains=search)
            if request.session.get('role')=='creator':
                return render(request,'creator/ss.html',{"data" : data,"tpost":tpost,"daypost":daypost})
            else:
                return render(request,'viewer/ss.html',{"data":data})

def likes(request):
    if request.session:
        if request.method=="GET":
            postid = request.GET.get("id")
            block = post.objects.get(postid=postid)
            if block.plike.filter(username=tbl_register.objects.get(username=request.session.get("username"))):
                block.plike.remove(tbl_register.objects.get(username=request.session.get("username")))
            else:
                block.plike.add(tbl_register.objects.get(username=request.session.get("username")))
            return redirect("home")
    return HttpResponse("<script>alert('you have to login first');location.href='/'</script>")


