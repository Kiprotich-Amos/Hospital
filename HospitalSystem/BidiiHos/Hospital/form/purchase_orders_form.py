from django.forms import ModelForm, DateInput, TextInput, NumberInput
from Hospital.models import PurchaseOrders

class PurchaseOrders_Form(ModelForm):
    class Meta:
        model = PurchaseOrders
        fields = '__all__'


        widgets ={
            'OrderID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' OrderID ', 'size': 10}),
            'SupplierID': TextInput(attrs={'class': 'form-control', 'id':'SupplierID'}),
            'OrderDate': DateInput(attrs={'class': 'form-control', 'id': 'OrderDate'}),
            'ExpectedDeliveryDate':DateInput(attrs={'class': 'form-control', 'id': 'ExpectedDeliveryDate'}),
            'TotalCost': NumberInput(attrs={'class': 'form-control', 'id': 'TotalCost'}),
            'OrderStatus': DateInput(attrs={'class': 'form-control', 'id': 'OrderStatus'}),
        }
        
        #   OrderID = models.AutoField(primary_key=True)
    # SupplierID = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    # OrderDate = models.DateField()
    # ExpectedDeliveryDate = models.DateField()
    # TotalCost = models.DecimalField(max_digits=10, decimal_places=2)
    # OrderStatus = models.CharField(max_length=255)