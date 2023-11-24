from django.forms import ModelForm, TextInput, NumberInput
from Hospital.models import Supplies

class Supplies_Form(ModelForm):
    class Meta:
        model = Supplies
        fields = '__all__'
        
        widgets ={
            'SupplyID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' SupplyID ', 'size': 10}),
            'SupplyName': TextInput(attrs={'class': 'form-control', 'id':'SupplyName'}),
            'Description': TextInput(attrs={'class': 'form-control', 'id': 'Description'}),
            'UnitPrice':NumberInput(attrs={'class': 'form-control', 'id': 'UnitPrice'}),
            'CurrentStock': NumberInput(attrs={'class': 'form-control', 'id': 'CurrentStock'}),
            'MinimumStock': NumberInput(attrs={'class': 'form-control', 'id': 'MinimumStock'}),
        }
        

        # class Supplies(models.Model):
    # SupplyID = models.AutoField(primary_key=True)
    # SupplyName = models.CharField(max_length=255)
    # Description = models.TextField()
    # UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    # CurrentStock = models.IntegerField()
    # MinimumStock = models.IntegerField()