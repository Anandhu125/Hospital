from django.urls import path

from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.SignView.as_view(), name='login'),
    path('register', views.SignUpView.as_view(), name='register'),
    path("home",views.IndexView.as_view(),name="index"),
    path("doctor",views.DoctorDetailView.as_view(),name="doc"),
    path("patient/edit/<int:id>",views.PatientUpdateView.as_view(),name="patient-edit"),
    path("contact/hospital",views.ContactView.as_view(),name="contact"),
    path("doctor/serach",views.DoctorSearchView.as_view(),name="serache-doctor"),
    path("logout",views.signout_view,name="signout")
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

