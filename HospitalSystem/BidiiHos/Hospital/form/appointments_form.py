from django.forms import ModelForm, TextInput,DateTimeInput
from Hospital.models import Appointments

class Appointments_Form(ModelForm):
    class Meta:
        model = Appointments
        fields = '__all__'

        widgets={
            'PatientID': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Patient ID'}),
            'DoctorID':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Doctor ID'}),
            'AppointmentDateTime':DateTimeInput(attrs={'class': 'label, form-control, form-label', 'id': 'AppointmentDateTime'}),
            'Notes':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'notes'}),
        }