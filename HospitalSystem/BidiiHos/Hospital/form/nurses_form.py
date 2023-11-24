from django.forms import ModelForm, TextInput
from Hospital.models import Nurses

class Nurses_Form(ModelForm):
    class Meta:
        model = Nurses
        fields = '__all__'

        
        widgets={
            'EmployeeID':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'EmployeeID '}),
            'NurseID': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'NurseID'}),
            # 'FirstName':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'FirstName '}),
            # 'LastName':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'LastName'}),
            'Specialization':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Specialization'}),
            # 'Phone':TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Phone'}),
            # 'Email':EmailInput(attrs={'class': 'label, form-control, form-label', 'id': 'Email'})
        }


    #      EmployeeID = EmployeeID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    # NurseID = models.AutoField(primary_key=True, unique=True)
    # Specialization = models.CharField(max_length=255)