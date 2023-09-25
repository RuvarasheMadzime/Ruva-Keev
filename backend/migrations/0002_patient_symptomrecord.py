# Generated by Django 4.2.5 on 2023-09-25 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('PATIENT_ID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('PATIENT_NAME', models.CharField(max_length=255)),
                ('PATIENT_AGE', models.IntegerField()),
                ('PATIENT_GENDER', models.CharField(max_length=10)),
                ('PATIENT_EMAIL', models.EmailField(max_length=254)),
                ('PATIENT_CONTACT_NUMBER', models.CharField(max_length=15)),
                ('MEDICAL_HISTORY', models.TextField()),
                ('PATIENT_ADDRESS', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SymptomRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('severity', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.patient')),
                ('symptom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.symptom')),
            ],
        ),
    ]
