from django.forms import ModelForm, TextInput, DateInput, EmailInput, NumberInput
from Hospital.models import Employees

class Employees_Form(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


        widgets ={
            'EmployeeID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' EmployeeID ', 'size': 10}),
            'FirstName': TextInput(attrs={'class': 'form-control', 'id': 'First Name'}),
            'LastName': TextInput(attrs={'class': 'form-control', 'id': 'Last Name'}),
            'DateOfBirth': DateInput(attrs={'class': 'form-control', 'id': 'Date Of Birth'}),
            'Employe_Id_Number':NumberInput(attrs={'class': 'form-control', 'id': 'Phone'}),
            'Gender': TextInput(attrs={'class': 'form-control', 'id': 'Gender'}),
            'Role': TextInput(attrs={'class': 'form-control', 'id': 'Role'}),
            'Address': TextInput(attrs={'class': 'form-control', 'id': 'Address'}),
            'Phone': TextInput(attrs={'class': 'form-control', 'id': 'Phone'}),
            'Email': EmailInput(attrs={'class': 'form-control', 'id': 'Email'}),
            'EmergencyContact': TextInput(attrs={'class': 'form-control', 'id': 'EmergencyContact'}),
        }
           