from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View #to make class view
from finance.forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form= RegisterForm()
        return render(request, 'finance/register.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form =RegisterForm(request.POST)
        if form.is_valid():
           user= form.save()
           login(request, user)
           redirect('dashboard')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')
    
    
    












 

'''# Create your views here. buisness logic
#function based view 
def home(request):
    return HttpResponse("<h1>Hello Django</h1>")

#class based view 
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello Django class</h1>")
    
#class based view with template
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finance/home.html')    
'''  

 
