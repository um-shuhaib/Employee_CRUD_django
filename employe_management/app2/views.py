from django.shortcuts import render,redirect
from employee.models import Employee
from django.views import View
from app2.forms import EmployeeForm
from django.http import HttpResponse

# Create your views here.
class EmpRegForm(View):
    def get(self,request):
        form=EmployeeForm()
        return render(request,"emp_reg.html",{"form":form})
    
    def post(self,request):
        form=EmployeeForm(request.POST)
        if form.is_valid():
            Employee.objects.create(**form.cleaned_data)
            return HttpResponse("<h3>data added</h3> <button>back to home</button>")
        else:
            return HttpResponse("invalid input")