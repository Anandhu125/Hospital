from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,ListView,UpdateView,TemplateView
from .models import Doctor,Appointment
from .forms import AdminSiginForm,AppointmentForm,DoctorForm,RegistrationForm,User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"please login")
            return redirect('login')
        else:
            return fn(request,*args, **kwargs)
    return wrapper

# Logout
def signout_view(request,*args, **kwargs):
    logout(request)
    return redirect("login")


# Register 
class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("login")

# Login
class SignView(View):
    def get(self,request,*args, **kwargs):
        form=AdminSiginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=AdminSiginForm(request.POST)
        
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":form})
            
            
# Home page
@method_decorator(signin_required,name="dispatch")
class IndexView(CreateView,ListView):
    model=Appointment
    form_class=AppointmentForm
    template_name="index.html"
    success_url=reverse_lazy("index")
    context_object_name="patient"
    
       
# Doctor Detail
@method_decorator(signin_required,name="dispatch")
class DoctorDetailView(CreateView,ListView):
    model=Doctor
    form_class=DoctorForm
    template_name="doctors-detail.html"
    success_url=reverse_lazy("doc")
    context_object_name="ho"


# patient Update
@method_decorator(signin_required,name="dispatch")   
class PatientUpdateView(UpdateView):
    model=Appointment
    form_class=AppointmentForm
    template_name="patientDetails-edit.html"
    success_url=reverse_lazy("index")
    pk_url_kwarg="id"

#  contact Details
@method_decorator(signin_required,name="dispatch")
class ContactView(TemplateView):
    template_name="contact.html"


# Doctor Search
@method_decorator(signin_required,name="dispatch")  
class DoctorSearchView(ListView,View):
    model=Doctor
    template_name="serach.html"
    context_object_name="doctor_post"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Doctor.objects.filter(doctor_Name_add__icontains=query).order_by('-doctor_Name_add')
    
    
    