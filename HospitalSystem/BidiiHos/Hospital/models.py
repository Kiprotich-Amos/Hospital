from django.db import models



class Departments(models.Model):
    DepartmentID = models.CharField(max_length=255, primary_key=True, unique= True)
    DepartmentName = models.CharField(max_length=255)
    vision = models.CharField(max_length=250)
    mission = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)


class Employees(models.Model):
    DepartmentID = models.ForeignKey(Departments, on_delete=models.CASCADE)
    EmployeeID = models.CharField(max_length=255, primary_key=True, unique= True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    DateOfBirth =  models.DateField()
    Employe_Id_Number =models.PositiveIntegerField()
    Gender = models.CharField(max_length=6, default=('Male','Female'))
    Role = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=15, default='+254')
    Email = models.EmailField(max_length=255)
    EmergencyContact = models.CharField(max_length=255)

class Patients(models.Model):
    PatientID = models.CharField(max_length=255, primary_key=True, default= 'PRLONGHOS/01/', unique=True)
    # PatientIdNo=models.IntegerField()
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=1)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=15,default='+254')
    Email = models.EmailField(max_length=255, default='      @gmail.com')
    InsuranceInfo = models.CharField(max_length=255)
    EmergencyContact = models.CharField(max_length=255)

class Doctors(models.Model):
    EmployeeID = EmployeeID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    DoctorID = models.AutoField(primary_key=True, unique=True)
    Specialization = models.CharField(max_length=255)

class Nurses(models.Model):
    EmployeeID = EmployeeID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    NurseID = models.AutoField(primary_key=True, unique=True, default= 'NRLONGHOS/01/')
    Specialization = models.CharField(max_length=255)

   
class Appointments(models.Model):
    AppointmentID = models.CharField(max_length=255, primary_key=True)
    PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    DoctorID = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    AppointmentDateTime = models.DateTimeField()
    Notes = models.TextField()

class MedicalRecords(models.Model):
    RecordID = models.CharField(max_length=255, primary_key=True)
    PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    AdmissionDate = models.DateField()
    DischargeDate = models.DateField()
    Diagnosis = models.TextField()
    Treatment = models.TextField()
    Prescriptions = models.TextField()

class Medications(models.Model):
    MedicationID = models.AutoField(primary_key=True)
    MedicationName = models.CharField(max_length=255)
    Dosage = models.CharField(max_length=255)
    UsageInstructions = models.TextField(max_length=255)

class Tests(models.Model):
    TestID = models.CharField(max_length=255,primary_key=True, unique=True)
    TestName = models.CharField(max_length=255)
    Description = models.TextField()
    Cost = models.DecimalField(max_digits=10, decimal_places = 2)

class TestResults(models.Model):
    ResultID = models.AutoField(primary_key=True, unique= True)
    TestID = models.ForeignKey(Tests, on_delete=models.CASCADE)
    PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    DoctorID = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    ResultDate = models.DateField()
    ResultDetails = models.TextField()

class Suppliers(models.Model):
    SupplierID = models.AutoField(primary_key=True, unique= True)
    SupplierName = models.CharField(max_length=255)
    ContactPerson = models.CharField(max_length=255)
    Phone = models.CharField(max_length=15, default='+254')
    Email = models.EmailField(max_length=255)
    Address = models.CharField(max_length=255)

class PurchaseOrders(models.Model):
    OrderID = models.CharField(max_length=255, primary_key=True, unique=True)
    SupplierID = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    OrderDate = models.DateField()
    ExpectedDeliveryDate = models.DateField()
    TotalCost = models.DecimalField(max_digits=10, decimal_places=2)
    OrderStatus = models.CharField(max_length=255)

class Supplies(models.Model):
    SupplyID = models.AutoField(primary_key=True, unique=True)
    SupplyName = models.CharField(max_length=255)
    Description = models.TextField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    CurrentStock = models.IntegerField()
    MinimumStock = models.IntegerField()

class PurchaseOrderItems(models.Model):
    ItemID = models.AutoField(primary_key=True, unique=True)
    OrderID = models.ForeignKey(PurchaseOrders, on_delete=models.CASCADE)
    SupplyID = models.ForeignKey(Supplies, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places = 2)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places  = 2)
    Date = models.DateTimeField()


class Payments(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentDate = models.DateField()
    PaymentMethod = models.CharField(max_length=255, default=('M-Pesa', 'Bank','Insurance', 'Check', 'Cash'))
    PaymentStatus = models.CharField(max_length=255, default=('Cleared', 'Pending', 'Invoiced'))

class Invoices(models.Model):
    InvoiceID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patients, on_delete=models.CASCADE)
    BillingDate = models.DateField()
    DueDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentStatus = models.CharField(max_length=255)


class EmployeeAttendance(models.Model):
    AttendanceID = models.AutoField(primary_key=True, unique=True)
    EmployeeID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    AttendanceDate = models.DateField()
    StartTime = models.TimeField()
    EndTime = models.TimeField()

class TaxCategories(models.Model):
    TaxCategoryID = models.AutoField(primary_key=True, unique=True)
    CategoryName = models.CharField(max_length=255)
    TaxRate = models.DecimalField(max_digits= 5, decimal_places=2)

class InvoiceTax(models.Model):
    InvoiceTaxID = models.AutoField(primary_key=True)
    InvoiceID = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    TaxCategoryID = models.ForeignKey(TaxCategories, on_delete=models.CASCADE)
    TaxAmount = models.DecimalField(max_digits=10, decimal_places=2)
