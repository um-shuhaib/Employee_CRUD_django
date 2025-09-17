from django.shortcuts import render,redirect
from django.views import View
from .models import Employee
# Create your views here.
class HomeView(View):
    def get(self,request):
        student=Employee.objects.all()
        return render(request,"home.html",{"student":student})
    
class EmpRegister(View):
    def get(self,request):
        return render(request,"register.html")
    
    def post(self,request):
        name=request.POST.get("name")
        salery=request.POST.get("salery")
        designation=request.POST.get("designation")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        Employee.objects.create(name=name,salery=salery,designation=designation,email=email,phone=phone)
        return redirect("home")

class UpdateEmp(View):
    def get(self,request,**kwargs):
        emp_id=kwargs.get("id")
        employee=Employee.objects.get(id=emp_id)
        return render(request,"update.html",{"employee":employee})
    
    def post(self,request,**kwargs):
        employee=Employee.objects.get(id=kwargs.get("id"))
        name=request.POST.get("name")
        salery=request.POST.get("salery")
        designation=request.POST.get("designation")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        
        employee.name=name
        employee.salery=salery
        employee.designation=designation
        employee.email=email
        employee.phone=phone

        employee.save()
        return redirect("home")
    
class DeleteEmp(View):
    def get(self,request,**kwargs):
        employee=Employee.objects.get(id=kwargs.get("id"))
        employee.delete()
        return redirect("home")