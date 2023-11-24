from django.shortcuts import render, redirect
from django.http import HttpResponse
import logging  # Import the logging module


# forms
from Hospital.form.patients_form import Patients_Form
from Hospital.form.doctors_form import Doctors_Form
from Hospital.form.appointments_form import Appointments_Form
from Hospital.form.medical_records_form import MedicalRecords_Form
from Hospital.form.departments_form import Departments_Form
from Hospital.form.nurses_form import Nurses_Form
from Hospital.form.medication_form import Medications_Form
from Hospital.form.tests_form import Tests_Form
from Hospital.form.test_results_form import TestResults_Form
from Hospital.form.suppliers_form import Suppliers_Form
from Hospital.form.purchase_orders_form import PurchaseOrders_Form
from Hospital.form.supplies_form import Supplies_Form
from Hospital.form.purchase_order_items_form import PurchaseOrderItems_Form
from Hospital.form.payments_form import Payments_Form
from Hospital.form.invoices_form import Invoices_Form
from Hospital.form.employees_form import Employees_Form
from Hospital.form.employee_attendance_form import EmployeeAttendance_Form
from Hospital.form.tax_categories_form import TaxCategories_Form
from Hospital.form.invoice_tax_form import InvoiceTax_Form

# models (use relative import)
from .models import *

logger = logging.getLogger('__name__')

patient = Patients.objects.all()


def base(request):
    return render(request, 'Hos/base.html')

def form(request):
    return render(request, 'Hos/Forms/form.html')

def dispaly():
     return HttpResponse('Saved Sucessfully')



def index(request):

    try:
        # Retrieve all patient records from the database
        patients = Patients.objects.all()
        p = patients.count()
        # print(patients)
        place_count = p 

        # Check if there are any patient records
        if patients.exists():
            context = {'patients': patients, 'place_count':place_count}
            return render(request, 'Hos/Dashboard/dashboard.html', context)
            
        else:
            # If there are no patients, return a message
            return render(request, 'no_patients.html')  # Create a template for this message

    except Exception as e:
         # Log the error for debugging
        logger.error(f"An error occurred in the 'index' view: {str(e)}")
        # Return a custom error page or message
        return HttpResponse('Error Loading')


def patients(request):
    try:
        if request.method == 'POST':
            patients_form = Patients_Form(request.POST)
            if patients_form.is_valid():
                patients_form.save()
                # Redirect to a successfully appointment page
                return redirect('appointments', patient_id=patient.PatientID)  # Removed 'context'

            elif request.method== 'POST':
                patient_id = request.POST.get("patient_id")
                print('patient_id')
            else:
                context = {'patients_form': patients_form}
                print(context)
                return HttpResponse('Check the data well and try again to submit')
        # If it's not a POST request or form is not valid, display the form
        patients_form = Patients_Form()
        patients_data = Patients.objects.all()
        patient_count = patients_data.count()

        context = {
            'patients_form': patients_form,
            'patient_count': patient_count,  # Pass the count to the template
        }
        return render(request, 'Hos/Forms/patients.html', context)
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def doctors(request):
    
    try:
        if request.method == 'POST':
            doctor_form = Doctors_Form(request.POST)
            if doctor_form.is_valid():
                doctor_form.save()
                return HttpResponse('Doctors Details saved successfuly')
            else:
                return HttpResponse('Cannot load data successfull ')
        doctor_form =  Doctors_Form()
        context = {'doctor_form': doctor_form}
        return render(request,'Hos/Forms/doctors.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def appointments(request, patient_id):
    try:
        patient = Patients.objects.get(PatientID=patient_id)
        if request.method == 'POST':
            appointments_form = Appointments_Form(request.POST)
            if appointments_form.is_valid():
                appointment = appointments_form.save(commit=False)  # Save appointment but don't commit yet
                appointment.patient = patient  # Associate the appointment with the patient
                appointment.save()  # Commit the appointment
                return HttpResponse("Data saved successfully")
        
        appointments_form = Appointments_Form()
        context = {
            'appointments_form': appointments_form,
            'patient': patient,
        }
        return render(request, 'Hos/Forms/appointments.html', context)
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html') 

def medical_records(request):
    try:
        if request.method == 'POST':
            medical_records_form = MedicalRecords_Form(request.POST)
            if medical_records_form.is_valid():
                medical_records_form.save()
                dispaly()

        medical_records_form = MedicalRecords_Form()
        context = {'medical_records_form': medical_records_form}
        return render(request, 'Hos/Forms/medical_records.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')
        
def departments(request):
    try:
        if request.method == 'POST':
            departments_form = Departments_Form(request.POST)
            if departments_form.is_valid():
                departments_form.save()
                # return render(request, 'Forms/departments.html')
                return render(request, 'Hos/Dashboard/index.html')
                # return HttpResponse("Saved Sucessfully")

            else:
                context = {'departments_form': departments_form}
                return render(request, 'Forms/departments.html', context)
        
        departments_form = Departments_Form()
        context = {'departments_form': departments_form}
        return render(request, 'Hos/Forms/departments.html', context)
  
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def nurses(request):
    try:
        if request.method == 'POST':
                nurses_form = Nurses_Form(request.POST)
                if nurses_form.is_valid():
                    nurses_form.save()


        nurses_form = Nurses_Form()
        context = {'nurses_form': nurses_form}

        return render(request, 'Hos/Forms/nurses.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def medications(request):
    try: 
        if request.method =='POST':
            medications_form = Medications_Form(request.POST)
            if medications_form.is_valid():
                medications_form.save()

        medications_form = Medications_Form()

        context ={'medications_form': medications_form}
        return render(request, 'Hos/Forms/medications.html', context)
    
    except Exception as e:
            print(e)
            return render(request, 'Hos/Errors/error404.html')

def tests(request):
    try:
        if request.method == 'POST': 
            tests_form = Tests_Form(request.post)

        tests_form = Tests_Form()

        context = {'tests_form' : tests_form}
        return render(request, 'Hos/Forms/tests.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def test_results(request):

    try: 
        if request.method =='POST':
            test_result_form = TestResults_Form(request.POST)
            if test_result_form.is_valid():
                test_result_form.save()
                return HttpResponse('Data saved successfuly')
            else:
                return HttpResponse('Data Error check before saving')

        
        test_result_form = TestResults_Form()
        context = {'test_result_form': test_result_form}
        return render(request, 'Hos/Forms/test_results.html', context)
    

    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def suppliers(request):
    try: 
        if request.method== 'POST':
            suppliers_form = Suppliers_Form(request.POST)
            if suppliers_form.is_valid():
                suppliers_form.save()
                return HttpResponse('Data saved successfuly')
            else:
                 return HttpResponse('Data Error check before saving')
        suppliers_form = Suppliers_Form()

        context = {'suppliers_form': suppliers_form}
        return render(request, 'Hos/Forms/suppliers.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def purchase_orders(request):
    try:
        if request.method == 'POST':
            purchase_orders_form = PurchaseOrders_Form(request.POST)
            if purchase_orders_form.is_valid():
                purchase_orders_form.save()
                dispaly()


        purchase_orders_form = PurchaseOrders_Form()

        context = {'purchase_orders_form': purchase_orders_form}
        return render(request, 'Hos/Forms/purchase_orders.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def supplies(request):
    try:
        if request.method == 'POST':
            supplies_form = Supplies_Form(request.POST)
            if supplies_form.is_valid():
                supplies_form.save()

        supplies_form = Supplies_Form()

        context = {'supplies_form': supplies_form}
        return render(request, 'Hos/Forms/supplies.html', context)
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def purchase_order_items(request):
    try:     
        if request.method =='POST':
            purchase_order_items_form = PurchaseOrderItems_Form(request.POST)
            if purchase_order_items_form.is_valid():
                purchase_order_items_form.save()
                return HttpResponse('payment received Sucessfully')
                
        purchase_order_items_form = PurchaseOrderItems_Form()
        context = {'purchase_order_items_form': purchase_order_items_form}
        return render(request, 'Hos/Forms/purchase_order_items.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def payments(request):
    try:     
        if request.method =='POST':
            payments_form = Patients_Form(request.POST)
            if payments_form.is_valid():
                payments_form.save()
                return HttpResponse('payment received Sucessfully')
            
        payments_form = Payments_Form()
        context = {'payments_form': payments_form}
        return render(request, 'Hos/Forms/payments.html', context)
    
    except Exception as e:
        print(e)
        return render(request, 'Hos/Errors/error404.html')

def invoices(request):

    try:
        if request.method == 'POST':
            invoices_form = Invoices_Form(request.POST)
            if invoices_form.is_valid():
                invoices_form.save()

        invoices_form = Invoices_Form()

        context = {'invoices_form': invoices_form}
        return render(request, 'Hos/Forms/invoices.html', context)
    
    except Exception as e:
        print(e)
        return HttpResponse('Hos/Error recording employees Try Again')

def employees(request):
    try:
        if request.method == 'POST':
           employees_form = Employees_Form(request.POST)
        employees_form = Employees_Form()

        context = {'employees_form': employees_form}
        return render(request, 'Hos/Forms/employees.html', context)
    
    except Exception as e:
        print(e)
        return HttpResponse('Error recording employees Try Again')

def employee_attendance(request):
    try:
        if request.method == 'POST':
            employee_attendance_form = EmployeeAttendance_Form(request.POST)
            if employee_attendance_form.is_valid():
                employee_attendance_form.save()
                return HttpResponse('Attendance recorded')
            

        employee_attendance_form = EmployeeAttendance_Form()

        context = {'employee_attendance_form ': employee_attendance_form}
        return render(request, 'Hos/Forms/employee_attendance.html', context)
            
    except Exception as e:
        print(e)
        return HttpResponse('Error recording Employe Attend ance Try Again')

def tax_categories(request):
    try:
        if request.method == 'POST':
            tax_categories_form = TaxCategories_Form(request.POST)
            if tax_categories_form.is_valid():
                tax_categories_form.save()
            # else
        tax_categories_form = TaxCategories_Form()
        context = {'tax_categories_form': tax_categories_form}
        return render(request, 'Hos/Forms/tax_categories.html', context)
    
    except Exception as e:
        print(e)
        return HttpResponse('Error recording Tax Category Try Again')

def invoice_tax(request):
    try:
        if request.method =='POST':
            invoice_tax_form = InvoiceTax_Form(request.POST)
            if invoice_tax_form.is_valid():
                invoice_tax_form.save()

        invoice_tax_form = InvoiceTax_Form()

        context = {'invoice_tax_form ': invoice_tax_form }
        return render(request, 'Hos/Forms/invoice_tax.html', context)
    
    except Exception as e:
        print(e)
        return HttpResponse('Error recording Tax Category Try Again')

