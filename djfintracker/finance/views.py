from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Sum, Q, Count
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.paginator import Paginator
from .forms import RegisterForm, TransactionForm, GoalForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction, Goal
from decimal import Decimal

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'finance/register.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Financial Tracker.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'finance/register.html', {'form': form})

class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Get all transactions for the user
        transactions = Transaction.objects.filter(user=request.user)
        
        # Calculate total income and expenses
        total_income = transactions.filter(transaction_type='Income').aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0.00')
        
        total_expense = transactions.filter(transaction_type='Expense').aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0.00')
        
        balance = total_income - total_expense
        
        # Get current month statistics
        current_month = timezone.now().replace(day=1)
        month_income = transactions.filter(
            transaction_type='Income',
            date__gte=current_month
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        month_expense = transactions.filter(
            transaction_type='Expense',
            date__gte=current_month
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Get recent transactions (last 5)
        recent_transactions = transactions.order_by('-date', '-id')[:5]
        
        # Get goals
        goals = Goal.objects.filter(user=request.user)
        active_goals = goals.filter(deadline__gte=timezone.now().date())
        
        # Calculate goal progress
        goal_progress = []
        total_income_all = transactions.filter(transaction_type='Income').aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0.00')
        
        for goal in active_goals:
            # Use total income for progress calculation
            saved_amount = total_income_all
            progress_percentage = min((saved_amount / goal.target_amount * 100), 100) if goal.target_amount > 0 else 0
            goal_progress.append({
                'goal': goal,
                'saved': saved_amount,
                'progress': progress_percentage
            })
        
        # Category breakdown for expenses
        category_expenses = transactions.filter(
            transaction_type='Expense'
        ).values('category').annotate(
            total=Sum('amount')
        ).order_by('-total')[:5]
        
        context = {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
            'month_income': month_income,
            'month_expense': month_expense,
            'recent_transactions': recent_transactions,
            'goal_progress': goal_progress,
            'category_expenses': category_expenses,
        }
        return render(request, 'finance/dashboard.html', context)
    
class TransactionCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'finance/transaction_form.html', {'form': form}) 
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            messages.success(request, f'Transaction "{transaction.title}" added successfully!')
            return redirect('transaction_list')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'finance/transaction_form.html', {'form': form})

class TransactionUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        form = TransactionForm(instance=transaction)
        return render(request, 'finance/transaction_form.html', {'form': form, 'transaction': transaction})
    
    def post(self, request, pk, *args, **kwargs):
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, f'Transaction "{transaction.title}" updated successfully!')
            return redirect('transaction_list')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'finance/transaction_form.html', {'form': form, 'transaction': transaction})

class TransactionDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
        title = transaction.title
        transaction.delete()
        messages.success(request, f'Transaction "{title}" deleted successfully!')
        return redirect('transaction_list')

class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'finance/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Transaction.objects.filter(user=self.request.user).order_by('-date', '-id')
        
        # Filter by transaction type
        transaction_type = self.request.GET.get('type')
        if transaction_type in ['Income', 'Expense']:
            queryset = queryset.filter(transaction_type=transaction_type)
        
        # Filter by category
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__icontains=category)
        
        # Filter by date range
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.filter(user=self.request.user)
        
        # Get unique categories for filter
        context['categories'] = transactions.values_list('category', flat=True).distinct()
        
        # Get filter values
        context['filter_type'] = self.request.GET.get('type', '')
        context['filter_category'] = self.request.GET.get('category', '')
        context['filter_date_from'] = self.request.GET.get('date_from', '')
        context['filter_date_to'] = self.request.GET.get('date_to', '')
        
        return context

class GoalCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = GoalForm()
        return render(request, 'finance/goal_form.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, f'Goal "{goal.name}" created successfully!')
            return redirect('goal_list')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'finance/goal_form.html', {'form': form})

class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = 'finance/goal_list.html'
    context_object_name = 'goals'
    
    def get_queryset(self):
        goals = Goal.objects.filter(user=self.request.user).order_by('deadline')
        transactions = Transaction.objects.filter(user=self.request.user)
        
        # Calculate progress for each goal
        goal_list = []
        total_income_all = transactions.filter(transaction_type='Income').aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0.00')
        
        for goal in goals:
            saved_amount = total_income_all
            progress_percentage = min((saved_amount / goal.target_amount * 100), 100) if goal.target_amount > 0 else 0
            remaining = max(goal.target_amount - saved_amount, Decimal('0.00'))
            
            goal_list.append({
                'goal': goal,
                'saved': saved_amount,
                'progress': progress_percentage,
                'remaining': remaining,
                'is_completed': saved_amount >= goal.target_amount,
                'is_overdue': goal.deadline < timezone.now().date() and saved_amount < goal.target_amount
            })
        
        return goal_list

class GoalUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        goal = get_object_or_404(Goal, pk=pk, user=request.user)
        form = GoalForm(instance=goal)
        return render(request, 'finance/goal_form.html', {'form': form, 'goal': goal})
    
    def post(self, request, pk, *args, **kwargs):
        goal = get_object_or_404(Goal, pk=pk, user=request.user)
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, f'Goal "{goal.name}" updated successfully!')
            return redirect('goal_list')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'finance/goal_form.html', {'form': form, 'goal': goal})

class GoalDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        goal = get_object_or_404(Goal, pk=pk, user=request.user)
        name = goal.name
        goal.delete()
        messages.success(request, f'Goal "{name}" deleted successfully!')
        return redirect('goal_list')

class ReportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(user=request.user)
        
        # Get filter parameters
        date_from = request.GET.get('date_from', '')
        date_to = request.GET.get('date_to', '')
        transaction_type = request.GET.get('type', '')
        category = request.GET.get('category', '')
        
        # Apply filters
        if date_from:
            transactions = transactions.filter(date__gte=date_from)
        if date_to:
            transactions = transactions.filter(date__lte=date_to)
        if transaction_type in ['Income', 'Expense']:
            transactions = transactions.filter(transaction_type=transaction_type)
        if category:
            transactions = transactions.filter(category__icontains=category)
        
        # Calculate statistics
        total_income = transactions.filter(transaction_type='Income').aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0.00')
        
        total_expense = transactions.filter(transaction_type='Expense').aggregate(
            total=Sum('amount')
        )['total'] or Decimal('0.00')
        
        net_balance = total_income - total_expense
        
        # Category breakdown
        income_by_category = transactions.filter(
            transaction_type='Income'
        ).values('category').annotate(
            total=Sum('amount'),
            count=Count('id')
        ).order_by('-total')
        
        expense_by_category = transactions.filter(
            transaction_type='Expense'
        ).values('category').annotate(
            total=Sum('amount'),
            count=Count('id')
        ).order_by('-total')
        
        # Monthly breakdown
        monthly_data = []
        monthly_raw = transactions.values('date__year', 'date__month').annotate(
            income=Sum('amount', filter=Q(transaction_type='Income')),
            expense=Sum('amount', filter=Q(transaction_type='Expense'))
        ).order_by('date__year', 'date__month')
        
        for month in monthly_raw:
            income = month['income'] or Decimal('0.00')
            expense = month['expense'] or Decimal('0.00')
            net = income - expense
            monthly_data.append({
                'year': month['date__year'],
                'month': month['date__month'],
                'income': income,
                'expense': expense,
                'net': net
            })
        
        context = {
            'transactions': transactions.order_by('-date'),
            'total_income': total_income,
            'total_expense': total_expense,
            'net_balance': net_balance,
            'income_by_category': income_by_category,
            'expense_by_category': expense_by_category,
            'monthly_data': monthly_data,
            'date_from': date_from,
            'date_to': date_to,
            'filter_type': transaction_type,
            'filter_category': category,
            'categories': Transaction.objects.filter(user=request.user).values_list('category', flat=True).distinct(),
        }
        return render(request, 'finance/report.html', context) 
        












 

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

 
