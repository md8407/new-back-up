from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from .forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import User
# from django.con import loginview
# from .models import Aemloyee
# Create your views here.


# class AddEmployee(ListView):
#     # model = 
    # template_name = 'templatemo_572_designer/index.html/'



def homepage(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'about.html')
    

def contact(request):
    return render(request,'contact.html')


def trend(request):
    return render(request,'trending.html')
    
def explore(request):
    return render(request,'explore.html') 

class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'employee/registration.html'
    success_url ="../login"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)  
        user.save()    
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + " - User Created Successfully..!!"

    
class UserLoginView(LoginView):
    template_name = 'employee/user_login.html'
    success_url ="/"


class ViewEmployee(ListView):
    model = User
    users = model.objects.all()
    context_object_name = "employees"
    template_name = "employee/view_employee.html"


