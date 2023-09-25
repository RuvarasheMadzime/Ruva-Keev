from rest_framework import serializers
from .models import Symptom, Patient, HealthTip
from .models import SymptomRecord

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'  # Include all fields/(the entity attributes) in the serialization


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'

class SymptomRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomRecord
        fields = '__all__'

class HealthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = '__all__'

