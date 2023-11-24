from django.forms import ModelForm, TextInput, NumberInput, DateInput
from Hospital.models import PurchaseOrderItems

class PurchaseOrderItems_Form(ModelForm):
    class Meta:
        model = PurchaseOrderItems
        fields = '__all__'


         
        widgets ={
            'OrderID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' OrderID ', 'size': 10}),
            'SupplyID': TextInput(attrs={'class': 'form-control', 'id':'SupplyID'}),
            'Quantity': TextInput(attrs={'class': 'form-control', 'id': 'Quantity'}),
            'UnitPrice':TextInput(attrs={'class': 'form-control', 'id': 'UnitPrice'}),
            'TotalPrice': TextInput(attrs={'class': 'form-control', 'id': 'TotalPrice'}),
            'Date': DateInput(attrs={'class': 'form-control', 'id': 'Date'}),
        }
        
    #       ItemID = models.AutoField(primary_key=True)
    # OrderID = models.ForeignKey(PurchaseOrders, on_delete=models.CASCADE)
    # SupplyID = models.ForeignKey(Supplies, on_delete=models.CASCADE)
    # Quantity = models.IntegerField()
    # UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    # TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)
