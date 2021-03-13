from django.db import models

# Create your models here.
class RegPeep(models.Model):

 EmailId = models.CharField(max_length = 50,blank = True)
 Username = models.CharField(max_length = 50,blank = True)
 Password = models.CharField(max_length = 50,blank = True)
 Gender = models.CharField(max_length = 50,blank = True)
 EnrollmentNo = models.IntegerField(blank =True,default=1)
 Branch = models.CharField(max_length = 50,blank=True)
 YearofStudy = models.CharField(max_length = 50,blank=True)
 I_SubjectCode = models.CharField(max_length = 50,blank=True)
 II_SubjectCode = models.CharField(max_length = 50,blank=True)
 III_SubjectCode = models.CharField(max_length = 50,blank=True)
 IV_SubjectCode = models.CharField(max_length = 50,blank=True)
 V_SubjectCode = models.CharField(max_length = 50,blank=True)
 VI_SubjectCode = models.CharField(max_length = 50,blank=True)
 VII_SubjectCode = models.CharField(max_length = 50,blank=True)
 VIII_SubjectCode = models.CharField(max_length = 50,blank=True)
       
 
 class Meta:
  db_table = "RegiPeep"
  
  


 