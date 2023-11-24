from django.forms import ModelForm, TextInput
from Hospital.models import Departments

class Departments_Form(ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'



        widgets={
            'DepartmentID': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'DepartmentID'}),
            'DepartmentName': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Department Name'}),
            'vision': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'vision'}),
            'mission': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'mission'}),
            'Description': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'Description'}),
        }

    #       DepartmentID = models.CharField(max_length=255, primary_key=True, unique= True)
    # DepartmentName = models.CharField(max_length=255)
    # vision = models.CharField(max_length=255)
    # mission = models.CharField(max_length=255)
    # Description = models.CharField(max_length=255)