from django.forms import ModelForm, TextInput, DateInput, EmailInput
from Hospital.models import Suppliers

class Suppliers_Form(ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'
        
        
        widgets ={
            'SupplierID ': TextInput(attrs={'class': 'label, form-control, form-label', 'id': ' SupplierID ', 'size': 10}),
            'SupplierName': TextInput(attrs={'class': 'form-control', 'id':'SupplierName'}),
            'ContactPerson': DateInput(attrs={'class': 'form-control', 'id': 'ContactPerson'}),
            'Phone': TextInput(attrs={'class': 'form-control', 'id': 'Phone'}),
            'Email': EmailInput(attrs={'class': 'form-control', 'id': 'Email'}),
            'Address': TextInput(attrs={'class': 'form-control', 'id': 'Address'}),

        }
        

        # class Suppliers(models.Model):
    # SupplierID = models.AutoField(primary_key=True)
    # SupplierName = models.CharField(max_length=255)
    # ContactPerson = models.CharField(max_length=255)
    # Phone = models.CharField(max_length=15, default='+254')
    # Email = models.EmailField(max_length=255)
    # Address = models.CharField(max_length=255)