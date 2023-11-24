from django.forms import ModelForm, TextInput,EmailInput
from Hospital.models import Doctors


class Doctors_Form(ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'

        widgets={
            'EmployeeID':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'EmployeeID '}),
            'DoctorID': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Doctor ID'}),
            # 'FirstName':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'FirstName '}),
            # 'LastName':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'LastName'}),
            'Specialization':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Specialization'}),
            # 'Phone':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Phone'}),
            # 'Email':EmailInput(attrs={'class': 'label, form-control, form-label', 'id': 'Email'})
        }