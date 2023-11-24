from django.forms import ModelForm, NumberInput, TextInput
from Hospital.models import TaxCategories

class TaxCategories_Form(ModelForm):
    class Meta:
        model = TaxCategories
        fields = '__all__'
 
        widgets ={
            'TaxCategoryID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' SupplyID ', 'size': 10}),
            'CategoryName': TextInput(attrs={'class': 'form-control', 'id':'CategoryName'}),
            'TaxRate': NumberInput(attrs={'class': 'form-control', 'id': 'Description'}),
            
        }
    #     class TaxCategories(models.Model):
    # TaxCategoryID = models.AutoField(primary_key=True)
    # CategoryName = models.CharField(max_length=255)
    # TaxRate = models.DecimalField(max_digits=5, decimal_places=2)