from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

doctors=[('dr.Venu(Cardiologist)','dr.Venu(Cardiologist)'),
         ('dr.Lekha(Dermatologists)','dr.Lekha(Dermatologists)'),
         ('dr.DD.Kuruvilla(Emergency Medicine specialists)','dr.DD.Kuruvilla(Emergency Medicine specialists)'),
         ('dr.Anu(Allergists/immunologists)','dr.Anu(Allergists/immunologists)'),
         ('dr.Vipin(Colon and Rectal Surgeons)','dr.Vipin(Colon and Rectal Surgeons)'),
         ('dr.Emy(ENT Specialist)','dr.Emy(ENT Specialist)'),
         ('dr.Athira(Gynecologist)','dr.Athira(Gynecologist)'),
         ('dr.Akhil(Radiologist)','dr.Akhil(Radiologist)'),
         ('dr.Vyshak(Oncologist)','dr.Vyshak(Oncologist)'),
         ('dr.Rekha(Orthopedic Surgeon)','dr.Rekha(Orthopedic Surgeon)'),
         ('dr.Abi(Veterinarian)','dr.Abi(Veterinarian)'),
    
]
    
class Doctor(models.Model):
    
    doctor_Name_add=models.CharField(max_length=30)
    photo= models.ImageField(upload_to='doctros',null=True,blank=True)
    department= models.CharField(max_length=50,null=True)
    qlification=models.CharField(max_length=99,null=True)

    
    def __str__(self):
        return self.doctor_Name_add

class Appointment(models.Model):
    Name=models.CharField(max_length=200,null=True)
    phone=models.PositiveIntegerField(null=True)
    Email=models.EmailField(null=True)
    address=models.CharField(max_length=300,null=True)
    doctor_Name=models.CharField(max_length=200,null=True,choices=doctors)
    Date=models.DateField(null=True,blank=True)
    place=models.CharField(max_length=300,null=True)
    time_slot=models.TimeField(null=True)
    app=[('Approved','Approved'),
         ('Rejected','Rejected'),
         ]
    status=models.CharField(max_length=200,null=True,choices=app,default='Approved')
    
    def __str__(self):
        return self.Name
    
    @property
    def upvote_count(self):
        return self.Name.all().count()
    
