from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from igem.forms import LoginForm
from igem.forms import DetailForm
from igem.forms import DetailForm2
from igem.forms import DetailForm3
from igem.models import RegPeep
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
#from django.views.generic.edit import FormView
from .forms import UploadFileForm
import os
from os import listdir
from os.path import isfile, join
from .forms import DeleteFileForm
from django.conf import settings
from django.core.mail import send_mail
from .forms import ForgotForm
from .forms import ChangePasswordForm
# Create your views here.

def firstpage(request):
 
 return render(request,'SignUp.html')
 
def signup(request):
 form = DetailForm(request.POST)
 if form.is_valid():
  global username
  username = form.cleaned_data['Username']
  emailId = form.cleaned_data['EmailId'] 
  password =form.cleaned_data['Password'] 
  gender = form.cleaned_data['Gender'] 
  
  o_ref = RegPeep(Username=username,EmailId=emailId,Password=password,Gender=gender)
  o_ref.save()
  
 return render(request,'SignUp2.html',{'form':form})
 
 
def signup2(request):
 form = DetailForm2(request.POST)
 if form.is_valid():
  enrollmentNo = form.cleaned_data['EnrollmentNo']
  branch = form.cleaned_data['Branch']
  yearofStudy = form.cleaned_data['YearofStudy']
  
  data = RegPeep.objects.filter(Username=username).update(
         EnrollmentNo = enrollmentNo,
         Branch = branch,
         YearofStudy = yearofStudy)
  
 return render(request,'SignUp3.html',{'form':form})
 
def signup3(request):
 
 form = DetailForm3(request.POST)
 if form.is_valid():
  ISubjectCode = form.cleaned_data['I_SubjectCode']
  IISubjectCode = form.cleaned_data['II_SubjectCode'] 
  IIISubjectCode = form.cleaned_data['III_SubjectCode']
  IVSubjectCode = form.cleaned_data['IV_SubjectCode']
  VSubjectCode = form.cleaned_data['V_SubjectCode']
  VISubjectCode = form.cleaned_data['VI_SubjectCode']
  VIISubjectCode = form.cleaned_data['VII_SubjectCode']
  VIIISubjectCode = form.cleaned_data['VIII_SubjectCode']
  
  data=RegPeep.objects.filter(Username=username).update(
       I_SubjectCode = ISubjectCode,
       II_SubjectCode = IISubjectCode,
       III_SubjectCode = IIISubjectCode,
       IV_SubjectCode = IVSubjectCode,
       V_SubjectCode = VSubjectCode,
       VI_SubjectCode = VISubjectCode,
       VII_SubjectCode = VIISubjectCode,
       VIII_SubjectCode = VIIISubjectCode)
  
  
 return HttpResponseRedirect('Login/',{'form':form})
 
class HomePage(TemplateView):
 template_name = 'Login.html'
 template_game = 'mainpage.html'
 
 def get(self,request,*args,**kwargs):
   MyLoginForm = LoginForm()
   return render(request,self.template_name,{'MyLoginForm':MyLoginForm})
 def post(self,request):
  
  MyLoginForm = LoginForm(request.POST)
  
  if MyLoginForm.is_valid():
   global user 
   userN = MyLoginForm.cleaned_data['usernam']
   userP = MyLoginForm.cleaned_data['Passwor']
   user = userN
   
   try:RegPeep.objects.only('Password').get(Password =userP); RegPeep.objects.only('Password').get(Username=userN)
   
   except RegPeep.DoesNotExist:return HttpResponseRedirect('/signup3/Login/')
   
   if RegPeep.objects.only('Password').get(Password =userP) == RegPeep.objects.only('Password').get(Username=user):
    txt = "login successful"
    return HttpResponseRedirect('/mainpage/',{'MyLoginForm':MyLoginForm})
   
  else:
   txt = "form not valid"
   return HttpResponseRedirect('/signup3/Login/',{'MyLoginForm':MyLoginForm})
  
def main(request,*args):
  
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)

 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub1)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 
 path = "igem/%s/%s/"%(user,sub2)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 
 path = "igem/%s/%s/"%(user,sub3)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 
 path = "igem/%s/%s/"%(user,sub4)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 
 path = "igem/%s/%s/"%(user,sub5)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 
 path = "igem/%s/%s/"%(user,sub6)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 
 path = "igem/%s/%s/"%(user,sub7)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 
 path = "igem/%s/%s/"%(user,sub8)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
 args = {'sub1':sub1,'gender':gender,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'mainpage.html',args)
 
 
"""def subject1(request,*args):
  
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 
 args = {'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 
 return render(request,'UploadsSub1.html',args)"""

 
            
"""class FileView(TemplateView):
 template_name = "UploadsSub1.html"
 
 def get(self,request,*args,**kwargs):
  form =uploadfileform()
  sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
  sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
  sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
  sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
  sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
  sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
  sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
  sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
  enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
  branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
  year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 
  args = {'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year,'form':form}
  return render(request,self.template_name,args)
   
 def post(self,request,*args,**kwargs):
  if request.method=='POST':
   form =uploadfileform(request.POST,request.FILES)
   if form.is_valid():
    form.save()
    txt ="form valid"
    return render_to_response('UploadsSub1.html',{'txt':txt})
   else:
    form=uploadfileform()
    txt ="form invalid"
    return render(request, 'UploadsSub1.html',{'txt':txt},{'form':form})

  else:
   txt ="method not post"
   return render(request,'UploadsSub1.html',{'txt':txt})"""
   
#handle_uploaded_file function defined here
def handle_uploaded_file(f):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub1)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)

#function for 1st subject page
def upload_file(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)

 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user)
  
 path = "igem/%s/%s/"%(user,sub1)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub1.html',args)

#function for 2nd subject page
def handle_uploaded_file2(f):
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub2)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)
   
def upload_file2(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user)
 
 path = "igem/%s/%s/"%(user,sub2)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file2(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload2/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub2.html',args)

#function for 3rd subject page
def handle_uploaded_file3(f):
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub3)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)
   
def upload_file3(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user)
 
 path = "igem/%s/%s/"%(user,sub3)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file3(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload3/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub3.html',args)

#function for 4th subject page
def handle_uploaded_file4(f):
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub4)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)   
def upload_file4(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user)
 
 path = "igem/%s/%s/"%(user,sub4)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file4(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload4/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub4.html',args)

#function for 5th subject page
def handle_uploaded_file5(f):
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub5)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)
   
def upload_file5(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user)
 
 path = "igem/%s/%s/"%(user,sub5)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file5(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload5/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub5.html',args)

#function for 6th subject page
def handle_uploaded_file6(f):
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub6)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)
   
def upload_file6(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user)
 
 path = "igem/%s/%s/"%(user,sub6)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file6(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload6/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub6.html',args)

#function for 7th subject page
def handle_uploaded_file7(f):
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub7)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)  
def upload_file7(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user) 
 path = "igem/%s/%s/"%(user,sub7)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file7(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload7/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub7.html',args)

#function for 8th subject page
def handle_uploaded_file8(f):
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 path = "igem/%s/%s/"%(user,sub8)
 with open(path +f.name, 'wb+') as destination:
  for chunk in f.chunks():
   destination.write(chunk)
   
def upload_file8(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user) 
 path = "igem/%s/%s/"%(user,sub8)
 try:
  os.makedirs(path)
 except FileExistsError:
  pass
  myfiles = os.listdir(path)
 if request.method =='POST':
  form = UploadFileForm(request.POST,request.FILES)
  args={}
  if form.is_valid():
   handle_uploaded_file8(request.FILES['file'])
   args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
   return redirect('/upload8/',args)
 else: 
  args={}
  form = UploadFileForm()
  args = {'form':form,'myfiles':myfiles,'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 return render(request,'UploadsSub8.html',args)
 
def ContactUs(request):
 sub1 = RegPeep.objects.values_list('I_SubjectCode',flat=True).get(Username=user)
 sub2 = RegPeep.objects.values_list('II_SubjectCode',flat=True).get(Username=user)
 sub3 = RegPeep.objects.values_list('III_SubjectCode',flat=True).get(Username=user)
 sub4 = RegPeep.objects.values_list('IV_SubjectCode',flat=True).get(Username=user)
 sub5 = RegPeep.objects.values_list('V_SubjectCode',flat=True).get(Username=user)
 sub6 = RegPeep.objects.values_list('VI_SubjectCode',flat=True).get(Username=user)
 sub7 = RegPeep.objects.values_list('VII_SubjectCode',flat=True).get(Username=user)
 sub8 = RegPeep.objects.values_list('VIII_SubjectCode',flat=True).get(Username=user)
 
 enrollmentno = RegPeep.objects.values_list('EnrollmentNo',flat=True).get(Username=user)
 branch = RegPeep.objects.values_list('Branch',flat=True).get(Username=user)
 year = RegPeep.objects.values_list('YearofStudy',flat=True).get(Username=user)
 gender = RegPeep.objects.values_list('Gender',flat=True).get(Username=user) 
 args = {'gender':gender,'sub1':sub1,'sub2':sub2,'sub3':sub3,'sub4':sub4,'sub5':sub5,'sub6':sub6,'sub7':sub7,'sub8':sub8,'user':user,'enrollmentno':enrollmentno,'branch':branch,'year':year}
 
 return render(request,'ContactUs.html',args)
 
def delete_file(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload/',{'form':form})
 
def delete_file2(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload2/',{'form':form})
 
def delete_file3(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload3/',{'form':form})
 
def delete_file4(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload4/',{'form':form})
 
def delete_file5(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload5/',{'form':form})
 
def delete_file6(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload6/',{'form':form})
 
def delete_file7(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload7/',{'form':form})
 
def delete_file8(request):
 if request.method == "POST":
  form = DeleteFileForm(request.POST)
  if form.is_valid():
   file_path=form.cleaned_data['FilePath']
   os.remove(file_path)
 else:
  form = DeleteFileForm()
 return redirect('/upload8/',{'form':form})
 
def ForgotPassword(request):
 if request.method == "POST":
  form = ForgotForm(request.POST)
  if form.is_valid():
   global name
   u_name = form.cleaned_data['uname']
   name=u_name
   emailto=RegPeep.objects.values_list('EmailId',flat=True).get(Username=name)
   res = send_mail("ChangePassword","Hi user click this link to change ur password.http://127.0.0.1:8000/change_password/",settings.EMAIL_HOST_USER,[emailto])
  else:
   form = ForgotForm()
 return render(request,'forgotpassword.html')
 
def change_password(request):
 if request.method=="POST":
  form = ChangePasswordForm(request.POST)
  if form.is_valid():
   u_password = form.cleaned_data['password']
   data = RegPeep.objects.filter(Username=name).update(Password=u_password)
   return redirect('/signup3/Login/')
 else:
  form= ChangePasswordForm()
  return render(request,'changepassword.html',{'name':name})

 