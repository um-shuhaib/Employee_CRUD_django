"""
URL configuration for employe_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views
from app2 import views as app2_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.HomeView.as_view(),name="home"),
    path("register",views.EmpRegister.as_view(),name="register"),
    path("update/<int:id>",views.UpdateEmp.as_view(),name="update"),
    path("delete/<int:id>",views.DeleteEmp.as_view(),name="delete"),
    path("app2/reg",app2_views.EmpRegForm.as_view(),name="empReg"),
    path("app2/update/<int:id>",app2_views.EmpupdateForm.as_view(),name="empupdate"),
    path("app2/modreg",app2_views.modelRegForm.as_view(),name="modreg"),
    path("app2/modup/<int:id>",app2_views.modelUpdateview.as_view(),name="modup"),
    


]
