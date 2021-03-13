from django import forms
from igem.models import RegPeep

class LoginForm(forms.Form):
 usernam = forms.CharField(max_length = 100)
 Passwor = forms.CharField(max_length=100)
 
class DetailForm(forms.Form):
 EmailId = forms.CharField(max_length = 50)
 Username = forms.CharField(max_length = 50)
 Password = forms.CharField(max_length = 50)
 Gender = forms.CharField(max_length = 50)
 
class DetailForm2(forms.Form):
 EnrollmentNo = forms.IntegerField()
 Branch = forms.CharField(max_length = 50)
 YearofStudy = forms.CharField(max_length = 50)
 
class DetailForm3(forms.Form):
 I_SubjectCode = forms.CharField(max_length = 50)
 II_SubjectCode = forms.CharField(max_length = 50)
 III_SubjectCode = forms.CharField(max_length = 50)
 IV_SubjectCode = forms.CharField(max_length = 50)
 V_SubjectCode = forms.CharField(max_length = 50)
 VI_SubjectCode = forms.CharField(max_length = 50)
 VII_SubjectCode = forms.CharField(max_length = 50)
 VIII_SubjectCode = forms.CharField(max_length = 50)
 
class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()
 
class DeleteFileForm(forms.Form):
  FilePath=forms.CharField(max_length= 1000)
 
class ForgotForm(forms.Form):
 uname= forms.CharField(max_length = 50)

class ChangePasswordForm(forms.Form):
 password = forms.CharField(max_length = 50) 
 

 
 