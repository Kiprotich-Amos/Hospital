from django.forms import ModelForm, TextInput, DateTimeInput
from Hospital.models import EmployeeAttendance

class EmployeeAttendance_Form(ModelForm):
    class Meta:
        model = EmployeeAttendance
        fields = '__all__'

        widgets={
            'AttendanceID': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'AttendanceID'}),
            'EmployeeID':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'EmployeeID'}),
            'AttendanceDate':DateTimeInput(attrs={'class': 'label, form-control, form-label', 'id': 'AttendanceDate'}),
            'StartTime':DateTimeInput(attrs={'class': 'label, form-control, form-label', 'id': 'StartTime'}),
            'EndTime':DateTimeInput(attrs={'class': 'label, form-control, form-label', 'id': 'EndTime'}),
        }

