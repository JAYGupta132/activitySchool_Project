from django.shortcuts import render, redirect
#for call models
from . import models
from adminapp.models import course,batch1
# from adminapp.models import models
#for file uploading ...
from django.core.files.storage import FileSystemStorage

# from studentapp.models import *
#for display image...
from django.conf import settings
media_url=settings.MEDIA_URL

from prj1.models import mstuser
#for date and time module
from datetime import date


#log out..............
from django.contrib.auth import logout

# Create your views here.
def adminhome(request):
    #for fatch session data.......................
    emailid=request.session.get("emailid")
    role=request.session.get("role")
    return render(request,"adminhome.html",{'emailid':emailid,'role':role})

def addcourse(request):
    if request.method=="POST":
        nm=request.POST.get("nm")
        duration=request.POST.get("duration")
        fees=request.POST.get("fees")
        coursedetail=request.POST.get("coursedetail")
        #for file uploading....
        courseicon=request.FILES["courseicon"]
        
        fs=FileSystemStorage()
        courseimg=fs.save(courseicon.name,courseicon)
        
        obj=models.course(nm=nm.strip(),duration=duration.strip(),fees=fees.strip(),coursedetail=coursedetail.strip(),courseicon=courseicon)
        obj.save()
        return render(request,"addcourse.html",{'msg':'Record Saved'})
    else:
        return render(request,"addcourse.html",{'msg':''})
    
def courselist1(request):
    if request.method=="GET":
        res=models.course.objects.all()
        return render(request, "courselist1.html", {'res':res})
    else:
        return render(request, "courselist1.html")

def studentlist(request):
    if request.method=="GET":
        res=mstuser.objects.filter(role="student")
        return render(request, "studentlist.html", {'res':res})
    
def batchentry1(request):
    if request.method=="POST":
        startdate=request.POST.get("startdate")
        batchtime=request.POST.get("batchtime")
        facultyname=request.POST.get("facultyname")
        batchstatus=1
        courseid=request.POST.get("courseid")
        obj=models.batch1(startdate=startdate,batchtime=batchtime.strip(),facultyname=facultyname,batchstatus=batchstatus,courseid_id=courseid)
        obj.save()
        return render(request,"batchentry1.html",{'obj':'','msg':'Record Saved'})
    else:
        obj=models.course.objects.all()
        return render(request,"batchentry1.html",{'obj':obj,'msg':''})

def logout1(request):
    logout(request)
    return redirect('http://localhost:8000/')

def editcourse(request):
    if request.method=="GET":
        courseid=request.GET.get("courseid") 
        res=models.course.objects.filter(courseid=courseid).values()
        return render(request,"editcourse.html",{'res':res})
    else:
        courseid=request.POST.get("courseid")
        nm=request.POST.get("nm")
        duration=request.POST.get("duration")
        fees=request.POST.get("fees")
    
        coursedetail=request.POST.get("coursedetail")
        models.course.objects.filter(courseid=courseid).update(courseid=courseid,nm=nm,duration=duration,fees=fees,coursedetail=coursedetail)
        return redirect("/adminhome/courselist1/")
    

def admissionstatus(request):
    if request.method=="GET":
        batchid=request.GET.get("batchid")
        #print(batchid)
        str1="""SELECT c.srno, c.emailid, a.batchid,a.admissionno,c.fnm,
a.emailid,c.fnm, a.admissiondate 
FROM studentapp_batchbooking as a 
inner join adminapp_batch1 as b on a.batchid=b.batchid 
INNER JOIN prj1_mstuser as c on a.emailid=c.emailid
        WHERE b.batchstatus=1"""
        print(str1)
        obj=batch1.objects.raw(str1)

        print(type(obj)) 
        return render(request,"admissionstatus.html",{'obj':obj})
    else:
        today = date.today()   
        admissiondate = today.strftime("%Y-%m-%d")
        emailid=request.session.get("emailid")
        batchid=request.POST.get("batchid")
        res1=batchid.objects.filter(emailid=emailid,batchid=batchid).exists()
        if res1==False:
            obj=batchid(batchid=batchid,admissiondate=admissiondate,emailid=emailid)
            obj.save()
            return render(request,"success.html",{'obj':'','msg':'you are succesfully registered for batch'})
        else: 
            return render(request,"success.html",{'obj':'','msg':'record already registered'})
