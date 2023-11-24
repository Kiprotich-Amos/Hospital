from django.forms import ModelForm, TextInput, DateInput
from Hospital.models import MedicalRecords

class MedicalRecords_Form(ModelForm):
     class Meta:
        model = MedicalRecords
        fields = '__all__'


        widgets ={
            'RecordID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' RecordID ', 'size': 10}),
            'PatientID': TextInput(attrs={'class': 'form-control', 'id': 'PatientID'}),
            'AdmissionDate': DateInput(attrs={'class': 'form-control', 'id': 'AdmissionDate'}),
            'DischargeDate': DateInput(attrs={'class': 'form-control', 'id': 'DischargeDate '}),
            'Diagnosis': TextInput(attrs={'class': 'form-control', 'id': 'Diagnosis'}),
            'Treatment': TextInput(attrs={'class': 'form-control', 'id': 'Role'}),
            'Prescriptions': TextInput(attrs={'class': 'form-control', 'id': 'Address'}),
        }

   #       RecordID = models.AutoField(primary_key=True)
   #  PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
   #  DoctorID = models.ForeignKey(Doctors, on_delete=models.CASCADE)
   #  AdmissionDate = models.DateField()
   #  DischargeDate = models.DateField()
   #  Diagnosis = models.TextField()
   #  Treatment = models.TextField()
   #  Prescriptions = models.TextField()