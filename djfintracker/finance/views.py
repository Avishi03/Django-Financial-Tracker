from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View #to make class view
from finance.forms import RegisterForm, TransactionForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form= RegisterForm()
        return render(request, 'finance/register.html', {'form':form})
    def post(self, request, *args, **kwargs):
        form =RegisterForm(request.POST)
        if form.is_valid():
           user= form.save()
           login(request, user)
        return redirect('dashboard')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')
    
class TransactionCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form= TransactionForm()
        return render(request, 'finance/transaction_form.html', {'form':form}) 
    def post(self, request, *args, **kwargs):
        form =TransactionForm(request.POST)
        if form.is_valid():
           transaction= form.save(commit=False)
           transaction.user= request.user
           transaction.save()
        return redirect('dashboard')
        return render(request, 'finance/transaction_form.html', {'form':form})
    
class TransactionListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions =Transaction.objects.all() #orm
        return render(request, 'finance/transaction_list.html', {'transactions':transactions}) 
        












 

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

 
