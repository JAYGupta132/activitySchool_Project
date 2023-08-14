from django.shortcuts import render,redirect
from. import models

from django.conf import settings
media_url=settings.MEDIA_URL
from adminapp.models import course


from . import emailAPI

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method=="POST":
        fnm=(request.POST.get("fnm"))
        gender=request.POST.get("gender")
        mno=request.POST.get("mno")
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        role="student"
        obj=models.mstuser(fnm=fnm.strip(),gender=gender,mno=mno.strip(),emailid=emailid.strip(),pwd=pwd.strip(),role=role.strip())
        obj.save()
        # for send verification email to registered email id
        emailAPI.sendMail(emailid, pwd)

        return render(request, "register.html",{'msg':'Profile created successfully..'})
    else:
        return render(request, "register.html",{'msg':''})
    
def login(request):
    if request.method=="POST":
        emailid=request.POST.get("emailid")
        pwd=request.POST.get("pwd")
        res=models.mstuser.objects.filter(emailid=emailid.strip(),pwd=pwd.strip())
        
        # print("role-",role)   for check login
        if len(res)>0:
            role=res[0].role
            #for session===============================================...
            request.session["emailid"]=emailid
            request.session["role"]=role
            #===========================================================
            if role=="admin":
                # print("Welcome admin")
                return redirect("/adminhome/")
            else:
                return redirect("/studenthome/")
        else:
            # return redirect("http://localhost/8000/")
            return render(request,"login.html",{'msg':'invalid emailid or password'})
        return render(request, "login.html",{'msg':''})
    else:
        return render(request, "login.html",{'msg':''})
    
def courselist2(request):
    if request.method=="GET":
        res=course.objects.all()
        return render(request, "courselist2.html", {'res':res, 'media_url':media_url})
    else:
        return render(request, "courselist2.html")
    
def gallery(request):
    return render(request,"gallery.html")