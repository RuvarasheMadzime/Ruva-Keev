from django.urls import path
from . import views
from .views import SymptomList, PatientList, HealthTipList

urlpatterns = [
    path('symptoms/', SymptomList.as_view(), name='symptom-list'),
    path('patients/', PatientList.as_view(), name='patient-list'), 
    path('symptom-records/', views.SymptomRecordList.as_view(), name='symptom-record-list'),
    path('symptom-records/<int:pk>/', views.SymptomRecordDetail.as_view(), name='symptom-record-detail'),
    path('health-tips/', HealthTipList.as_view(), name='health-tip-list')   
]

