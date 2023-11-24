from django.forms import ModelForm, TextInput,DateInput
from Hospital.models import Invoices
 
class Invoices_Form(ModelForm):
    class Meta:
        model =Invoices
        fields = '__all__'

        widgets ={
            # 'EmployeeID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' EmployeeID ', 'size': 10}),
            'PatientID': TextInput(attrs={'class': 'form-control', 'id': 'PatientID'}),
            'BillingDate': DateInput(attrs={'class': 'form-control', 'id': 'BillingDate'}),
            'DueDate':DateInput(attrs={'class': 'form-control', 'id': 'DueDate'}),
            'TotalAmount': TextInput(attrs={'class': 'form-control', 'id': 'TotalAmount'}),
            'PaymentStatus': TextInput(attrs={'class': 'form-control', 'id': 'PaymentStatus'}),
        }

        #  InvoiceID = models.AutoField(primary_key=True)
    # PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    # BillingDate = models.DateField()
    # DueDate = models.DateField()
    # TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    # PaymentStatus = models.CharField(max_length=255) 