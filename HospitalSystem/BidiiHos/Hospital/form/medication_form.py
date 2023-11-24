from django.forms import ModelForm,TextInput, DateTimeInput
from Hospital.models import Medications

class Medications_Form(ModelForm):
    class Meta:
        model = Medications
        fields = '__all__'


        widgets={
            'MedicationName': TextInput(attrs={'class': 'label, form-control, form-label', 'id': 'MedicationName'}),
            'Dosage':TextInput(attrs={'class': 'label, form-control', 'id': 'Dosage'}),
            'UsageInstructions':DateTimeInput(attrs={'class': 'label, form-control, form-label', 'id': 'UsageInstructions'}),
        }