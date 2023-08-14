from django.shortcuts import render,redirect
from adminapp.models import course
from adminapp.models import batch1
from prj1.models import *

from studentapp.models import batchbooking

#for display image...
from django.conf import settings
media_url=settings.MEDIA_URL

#for logout
from django.contrib.auth import logout

#for date and time module
from datetime import date

def sessioncheckstud_middleware(get_response):
 def middleware(request):
    if request.path=='/studenthome/' or request.path=='/studenthome/batchlist2/' or request.path=='/studenthome/addmission/' :
        if request.session["emailid"]==None or request.session["role"]!="student":
            response=redirect('/login/')
        else:
            response=get_response(request)
    else:
        response=get_response(request)
    return response
 return middleware 


# Create your views here.
def studenthome(request):
    #for fetch session data
    emailid=request.session.get("emailid")
    role=request.session.get("role")        
    return render(request,"studenthome.html",{'emailid':emailid,'role':role})

def courselist3(request):
    obj=course.objects.all()
    return render(request,"courselist3.html",{'obj':obj}) 

def batchlist2(request):
    if request.method=="GET":
        s="""select a.batchid,b.courseid,
        b.nm,b.duration,b.fees,
        a.startdate,a.batchtime,
        a.facultyname
        from adminapp_batch1 as a
        inner join adminapp_course as b 
        on a.courseid_id=b.courseid
        where a.batchstatus=1"""
        obj=course.objects.raw(s)
        print(type(obj))    
        return render(request,"batchlist2.html",{'obj':obj})         
 
def admission(request):
    if request.method=="GET":
        batchid=request.GET.get("batchid")
        #print(batchid)
        s="""select a.batchid,b.courseid,
        b.nm,b.duration,b.fees,
        a.startdate,a.batchtime,a.facultyname
        from adminapp_batch1 as a
        inner join adminapp_course as b on a.courseid_id=b.courseid
        where a.batchid=""" + batchid
        obj=course.objects.raw(s)
        print(type(obj)) 
        return render(request,"admission.html",{'obj':obj})          
    else:
        today = date.today()   
        admissiondate = today.strftime("%Y-%m-%d")
        emailid=request.session.get("emailid")
        batchid=request.POST.get("batchid")
        res1=batchbooking.objects.filter(emailid=emailid,batchid=batchid).exists()
        if res1==False:
            obj=batchbooking(batchid=batchid,admissiondate=admissiondate,emailid=emailid)
            obj.save()
            return render(request,"success.html",{'obj':'','msg':'you are succesfully registered for batch'})
        else: 
            return render(request,"success.html",{'obj':'','msg':'record already registered'})
   
def logout2(request):
    logout(request)
    return redirect('http://localhost:8000/')   

def batchstatus(request):
    emailid=request.session.get("emailid")
    obj=batchbooking.objects.filter(emailid=emailid)
    return render(request,"batchstatus.html",{'obj':obj}) 
