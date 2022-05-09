from django.shortcuts import render
#from emp_project.testapp.models import Department, Role

# Create your views here.
from testapp.models import Employee,Department,Role
def department_info_view(request):
    departments = Department.objects.all()
    return render(request,'testapp/index.html',{'departments':departments})
def role_info_view(request):
    roles = Role.objects.all()
    return render(request,'testapp/index.html',{'roles':roles})




# Create your views here.
def employee_info_view(request):
    employees = Employee.objects.all()
    return render(request,'testapp/index.html',{'employees':employees})
