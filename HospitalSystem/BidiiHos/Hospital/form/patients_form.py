# from django.forms import ModelForm, TextInput, EmailInput, NumberInput,DateInput
# from Hospital.models import Patients

# class Patients_Form(ModelForm):
#     class Meta:
#         model = Patients
#         fields = '__all__'

#         widgets ={
#             'PatientID': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Patient ID', 'size': 10}),
#             'FirstName': TextInput(attrs={'class': 'form-control', 'id': 'First Name'}),
#             'LastName': TextInput(attrs={'class': 'form-control', 'id': 'Last Name'}),
#             'DateOfBirth': DateInput(attrs={'class': 'form-control', 'id': 'Date Of Birth'}),
#             'Gender': TextInput(attrs={'class': 'form-control', 'id': 'Gender'}),
#             'Address': TextInput(attrs={'class': 'form-control', 'id': 'Address'}),
#             'Phone': TextInput(attrs={'class': 'form-control', 'id': 'Phone'}),
#             'Email': EmailInput(attrs={'class': 'form-control', 'id': 'Email'}),
#             'InsuranceInfo': TextInput(attrs={'class': 'form-control', 'id': 'InsuranceInfo'}),
#             'EmergencyContact': TextInput(attrs={'class': 'form-control', 'id': 'EmergencyContact'}),
#         }
from django import forms
from Hospital.models import Patients

class Patients_Form(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        widgets = {
            'PatientID': forms.TextInput(attrs={'class': 'form-control', 'id': 'patient-id'}),
            'FirstName': forms.TextInput(attrs={'class': 'form-control', 'id': 'first-name'}),
            'LastName': forms.TextInput(attrs={'class': 'form-control', 'id': 'last-name'}),
            'DateOfBirth': forms.DateInput(attrs={'class': 'form-control', 'id': 'date-of-birth'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control', 'id': 'gender'}),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address'}),
            'Phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'InsuranceInfo': forms.TextInput(attrs={'class': 'form-control', 'id': 'insurance-info'}),
            'EmergencyContact': forms.TextInput(attrs={'class': 'form-control', 'id': 'emergency-contact'}),
        }
