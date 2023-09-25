from django.db import models


class Symptom(models.Model):
    SYMPTOM_ID = models.AutoField(primary_key=True)
    SYMPTOM_NAME = models.CharField(max_length=255)
    SYMPTOM_DESCRIPTION = models.TextField()
    SEVERITY_OF_SYMPTOM = models.CharField(max_length=20)
    DURATION_OF_SYMPTOM = models.CharField(max_length=20)

    def __str__(self):
        return self.SYMPTOM_NAME

    class Meta:
        app_label='backend' #this specifies the app label


class Patient(models.Model):
    PATIENT_ID = models.CharField(max_length=255, primary_key=True)
    PATIENT_NAME = models.CharField(max_length=255)
    PATIENT_AGE = models.IntegerField()
    PATIENT_GENDER = models.CharField(max_length=10)
    PATIENT_EMAIL = models.EmailField()
    PATIENT_CONTACT_NUMBER = models.CharField(max_length=15)
    MEDICAL_HISTORY = models.TextField()
    PATIENT_ADDRESS = models.TextField()

    class Meta:
        app_label='backend' #this specifies the app label

    def __str__(self):
        return self.PATIENT_NAME


class HealthTip(models.Model):
    TIP_TITLE = models.CharField(max_length=255)
    TIP_CONTENT = models.TextField()
    TIP_TYPE = models.CharField(max_length=50)
    
    class Meta:
        app_label='backend' #this specifies the app label

    def __str__(self):
        return self.TIP_TITLE

class SymptomRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length=20)

    class Meta:
        app_label = 'backend' 

    def __str__(self):
        return f"{self.patient} - {self.symptom} - {self.record_date}"
    



