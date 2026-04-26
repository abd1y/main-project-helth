from django.urls import path
from .views import GetAllDiseases,GetAllEmergency
urlpatterns = [
    path('Diseases/',GetAllDiseases),
    path('Emergency/',GetAllEmergency),
    
]