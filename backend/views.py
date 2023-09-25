from django.shortcuts import render
from rest_framework import generics
from .models import Symptom, Patient, HealthTip
from .models import SymptomRecord
from .serializers import SymptomSerializer, PatientSerializer, HealthTipSerializer
from .serializers import SymptomRecordSerializer


class SymptomList(generics.ListCreateAPIView):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class HealthTipList(generics.ListCreateAPIView):
    queryset = HealthTip.objects.all()
    serializer_class = HealthTipSerializer


class SymptomRecordList(generics.ListCreateAPIView):
    queryset = SymptomRecord.objects.all()
    serializer_class = SymptomRecordSerializer


#I think I wont need the one below
class SymptomRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SymptomRecord.objects.all()
    serializer_class = SymptomRecordSerializer