import datetime
import uuid

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Q


from . models import User_register
from .models import BlogTable
from .models import commenttable
from .models import usertag




# Create your views here.

def base(request):
    return render(request,'blogapp/base.html')


def about(request):
    return render(request,'blogapp/about.html')

def contact(request):
    return render(request,'blogapp/contact.html')


@login_required(login_url='/')
def home(request):
    
    data=BlogTable.objects.all()
    data1=commenttable.objects.filter(is_delete=False)
    
    
    
        
    return render(request,'blogapp/home.html',{'data':data,'data1':data1})
 
 
def blogcomment(request,pk):
    
    if request.method=="POST":
        blogcomment=request.POST['blogcomment']
        username=request.user.username
        
        commenttable.objects.create(comment_id=pk,comment_time=datetime.datetime.now(),
                                    comment_by=username,cmt=blogcomment)
        
    data=BlogTable.objects.all()
    data1=commenttable.objects.filter(is_delete=False)
    return render(request,'blogapp/home.html',{'data':data,'data1':data1})
       

def cmtdelete(request,pk):
    cmt=commenttable.objects.get(id=pk)
    cmt.is_delete=True
    cmt.save()
    return redirect("/home")


def cmtedit(request,pk):
    cmt1=commenttable.objects.get(id=pk)
    
    if request.method == "POST":
        cmt=request.POST['blogcomment']
        commenttable.objects.filter(id=pk).update(cmt=cmt)
        return redirect("/home")
    
    return render(request,'blogapp/editcmt.html',{'cmt1':cmt1})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        # username1=User_register.objects.filter(username=username)
        # if not username1:
        #     err={"invalid username and password":""}
        #     return render(request,'blogapp/login.html',{'err':err})
            
        # for data in username1:
        #     username2=data.username
        #     password2=data.password
            
        #     if username2 == username and password2==password:
        #         return redirect("/home")
            
        #     else:
        #         err={"invalid username and password":""}
        #         return render(request,'blogapp/login.html',{'err':err})
        
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("/home")
        else:
            logout(request)
            err={"invalid username and password":""}
            return render(request,'blogapp/login.html',{'err':err})
        
        
    return render(request,'blogapp/login.html')

def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        gender=request.POST['gender']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password != confirmpassword:
            pas={"error ! enter same password":""}
            return render(request,'blogapp/register.html',{'pas':pas})
        
        User_register.objects.create(firstname=firstname,lastname=lastname,gender=gender,
                                     email=email,username=username,password=password)
        User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        
        
    return render(request,'blogapp/register.html')



def user_logout(request):
    logout(request)
    
    return redirect("/")



@login_required(login_url='/')
def profile(request):
    data=BlogTable.objects.filter(username=request.user.username)
    tt=usertag.objects.filter(tag_to=request.user.username)
    r=[i.tagid for i in tt]
    tagblog=BlogTable.objects.filter(reference_id__in= r)  
    data1=commenttable.objects.filter(is_delete=False)
    return render(request,'blogapp/profile.html',{'data':data,'data1':data1,'tagblog':tagblog})
   
 
def generate_uuid():
    return uuid.uuid4().hex 
  
def usertag1(request):
    pid=generate_uuid()
    user=User.objects.first()
    user1=User.objects.all()
    try:
        if request.method=="POST":
            title=request.POST['title']
            username=request.user.username
            firstname=request.user.first_name
            lastname=request.user.last_name
            
            
            
            BlogTable.objects.create(title=title,reference_id=pid,firstname=firstname,lastname=lastname,
                                    created_by=user,created_at=datetime.datetime.now(),username=username)
        data=BlogTable.objects.filter(reference_id=pid)
         
        
    except:
        pass       
    return render(request,"blogapp/usertag.html",{"data":data,"user1":user1})  



def bio(request,pk):
    if request.method=="POST":
        description=request.POST['description']
        image=request.POST['image']
        BlogTable.objects.filter(reference_id=pk).update(description=description,image=image)
        
    data=BlogTable.objects.filter(reference_id=pk)
    user1=User.objects.all()
    return render(request,"blogapp/usertag.html",{"data":data,"user1":user1})


def tagu(request,pk):
    bt=BlogTable.objects.get(reference_id=pk)
    bt1=bt.title
    if request.method=="POST":
        tag_to=request.POST['tag_to']
        usertag.objects.create(tag_to=tag_to,tag_by=request.user.username,tagid=pk,tag_title=bt1)
        
    user1=User.objects.all()
    data=BlogTable.objects.filter(reference_id=pk)
    return render(request,"blogapp/usertag.html",{"data":data,"user1":user1})

@login_required(login_url='/')     
def searchbar(request):
    # for search funtionality
    searched = request.GET.get('search')

    if searched:
        results = User_register.objects.filter(
            Q(firstname__icontains=searched) | Q(lastname__icontains=searched))
    else:
        results = User_register.objects.none()

    return render(request, 'blogapp/home.html', {'results': results, 'searched': searched})



def searchprofile(request,pk):
   
    searchid=User_register.objects.get(id=pk)
    searchuser=searchid.username
    data=BlogTable.objects.filter(username=searchuser)
    
    tt=usertag.objects.filter(tag_to=searchuser)
    r=[i.tagid for i in tt]
    tagblog=BlogTable.objects.filter(reference_id__in= r)
        
   
    
    
    data1=commenttable.objects.filter(is_delete=False)
    
    
    
        
    return render(request,'blogapp/searchprofile.html',{'data':data,'data1':data1,'tagblog':tagblog})