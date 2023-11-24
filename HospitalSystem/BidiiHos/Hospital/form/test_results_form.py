from django.forms import ModelForm, TextInput, DateInput
from Hospital.models  import TestResults

class TestResults_Form(ModelForm):
    class Meta:
        model = TestResults
        fields = '__all__'


        widgets ={
            'TestID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' TestID ', 'size': 10}),
            'PatientID': TextInput(attrs={'class': 'form-control', 'id': 'PatientID'}),
            'DoctorID': TextInput(attrs={'class': 'form-control', 'id': 'DoctorID'}),
            'ResultDate': DateInput(attrs={'class': 'form-control', 'id': 'ResultDate'}),
            'ResultDetails':TextInput(attrs={'class': 'form-control', 'id': 'ResultDetails'}),
            # 'Gender': TextInput(attrs={'class': 'form-control', 'id': 'Gender'}),
            # 'Role': TextInput(attrs={'class': 'form-control', 'id': 'Role'}),
            # 'Address': TextInput(attrs={'class': 'form-control', 'id': 'Address'}),
            # 'Phone': TextInput(attrs={'class': 'form-control', 'id': 'Phone'}),
            # 'Email': EmailInput(attrs={'class': 'form-control', 'id': 'Email'}),
            # 'EmergencyContact': TextInput(attrs={'class': 'form-control', 'id': 'EmergencyContact'}),
        }

        # class TestResults(models.Model):
    # ResultID = models.AutoField(primary_key=True)
    # TestID = models.ForeignKey(Tests, on_delete=models.CASCADE)
    # PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    # DoctorID = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    # ResultDate = models.DateField()
    # ResultDetails = models.TextField()
