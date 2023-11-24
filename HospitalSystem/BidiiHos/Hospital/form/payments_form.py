from django.forms import ModelForm, NumberInput, TextInput, DateInput
from Hospital.models import Payments

class Payments_Form(ModelForm):
    class Meta:
        model =Payments
        fields = '__all__'
        


        
        widgets ={
            'PatientID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' PatientID ', 'size': 10}),
            'Amount': NumberInput(attrs={'class': 'form-control', 'id':'Amount'}),
            'PaymentDate': DateInput(attrs={'class': 'form-control', 'id': 'PaymentDate'}),
            'PaymentMethod':TextInput(attrs={'class': 'form-control', 'id': 'PaymentMethod'}),
            'PaymentStatus': TextInput(attrs={'class': 'form-control', 'id': 'PaymencyContact'}),
        }
        

    #       PaymentID = models.AutoField(primary_key=True)
    # PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    # # Amount = models.DecimalField(max_digits=10, decimal_places=2)
    # PaymentDate = models.DateField()
    # PaymentMethod = models.CharField(max_length=255)
    # PaymentStatus = models.CharField(max_length=255)