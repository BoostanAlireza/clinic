from django.db import models

class PatientPersonalInfo(models.Model):
    file_number = models.IntegerField(unique=True)
    identification_number = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=50)
    phone = models.IntegerField()
    mobile_phone = models.IntegerField()
    address = models.TextField(null=True, blank=True)

    # def __str__(self) -> str:
    #     return self.first_name + ' ' + self.last_name

    

# class Introducer(models.Model):
#     introducer_name = models.CharField(max_length=50)


class Medical_history(models.Model):
    ailment = models.CharField(max_length=50)
    hospitalization_history = models.CharField(max_length=50)
    hospitalization_cause = models.TextField(null=True, blank=True)
    medication_use = models.CharField(max_length=50)
    patient = models.OneToOneField(PatientPersonalInfo, on_delete=models.CASCADE)


class TreatmentSession(models.Model):
    date = models.DateField(null=True, blank=True, auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    invoice = models.IntegerField()
    payment = models.IntegerField()
    balance = models.IntegerField()
    doctor = models.CharField(max_length=50)
    patient = models.OneToOneField(PatientPersonalInfo, on_delete=models.CASCADE)