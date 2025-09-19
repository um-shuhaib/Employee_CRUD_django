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
        
class EmpupdateForm(View):
    def get(self,request,**kwargs):
        emp=Employee.objects.get(id=kwargs.get("id"))
        form=EmployeeForm(initial={"name":emp.name,"salery":emp.salery,"designation":emp.designation,"email":emp.email,"phone":emp.phone})
        return render(request,"emp_reg.html",{"form":form})
    
    def post(self,request,**kwargs):
        emp=Employee.objects.get(id=kwargs.get("id"))
        form=EmployeeForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            salery=form.cleaned_data.get("salery")
            designation=form.cleaned_data.get("designation")
            email=form.cleaned_data.get("email")
            phone=form.cleaned_data.get("phone")
            emp.name=name
            emp.salery=salery 
            emp.designation=designation 
            emp.email=email
            emp.phone=phone 
            emp.save()
            return redirect("home")