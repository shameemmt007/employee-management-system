from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from .forms import EmployeeForm
from .models import Employee

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')




def add_employee(request):

    if request.method == 'POST':

        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})





def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        'employee_list.html',
        {'employees': employees}
    )