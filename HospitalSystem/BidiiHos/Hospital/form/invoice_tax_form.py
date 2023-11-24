from django.forms import ModelForm, TextInput,DateInput
from Hospital.models import InvoiceTax

class InvoiceTax_Form(ModelForm):
    class Meta:
        model = InvoiceTax
        fields = '__all__'

    
        widgets ={
            # 'EmployeeID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' EmployeeID ', 'size': 10}),
            'InvoiceID': TextInput(attrs={'class': 'form-control', 'id': 'InvoiceID'}),
            'TaxCategoryID': TextInput(attrs={'class': 'form-control', 'id': 'TaxCategoryID'}),
            'TaxAmount': TextInput(attrs={'class': 'form-control', 'id': 'TaxAmount'}),
            'Date':DateInput(attrs={'class': 'form-control', 'id': 'Date'}),
        }
           
    #        InvoiceTaxID = models.AutoField(primary_key=True)
    # # InvoiceID = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    # # TaxCategoryID = models.ForeignKey(TaxCategories, on_delete=models.CASCADE)
    # TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)