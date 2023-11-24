from django.forms import ModelForm, TextInput, NumberInput
from Hospital.models import Tests

class Tests_Form(ModelForm):
    class Meta:
        model = Tests
        fields = '__all__'


        
        widgets ={
            'TestID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' TestID ', 'size': 10}),
            'TestName': TextInput(attrs={'class': 'form-control', 'id': 'TestName'}),
            'Description': TextInput(attrs={'class': 'form-control', 'id': 'Description'}),
            'Cost': NumberInput(attrs={'class': 'form-control', 'id': 'Cost'}),
            # 'ResultDetails':TextInput(attrs={'class': 'form-control', 'id': 'ResultDetails'}),
            # 'Gender': TextInput(attrs={'class': 'form-control', 'id': 'Gender'}),
            # 'Role': TextInput(attrs={'class': 'form-control', 'id': 'Role'}),
            # 'Address': TextInput(attrs={'class': 'form-control', 'id': 'Address'}),
            # 'Phone': TextInput(attrs={'class': 'form-control', 'id': 'Phone'}),
            # 'Email': EmailInput(attrs={'class': 'form-control', 'id': 'Email'}),
            # 'EmergencyContact': TextInput(attrs={'class': 'form-control', 'id': 'EmergencyContact'}),
        }


        # class Tests(models.Model):
    # TestID = models.CharField(max_length=255,primary_key=True)
    # TestName = models.CharField(max_length=255)
    # Description = models.TextField()
    # Cost = models.DecimalField(max_digits=10, decimal_places=2)