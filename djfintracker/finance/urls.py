from django.urls import path, include
from finance.views import (
    RegisterView, DashboardView, 
    TransactionCreateView, TransactionListView, TransactionUpdateView, TransactionDeleteView,
    GoalCreateView, GoalListView, GoalUpdateView, GoalDeleteView,
    ReportView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('', DashboardView.as_view(), name="dashboard"),
    
    # Transaction URLs
    path('transaction/add/', TransactionCreateView.as_view(), name='transaction_add'),
    path('transaction/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction_edit'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('transaction/', TransactionListView.as_view(), name='transaction_list'),
    
    # Goal URLs
    path('goal/add/', GoalCreateView.as_view(), name='goal_add'),
    path('goal/<int:pk>/edit/', GoalUpdateView.as_view(), name='goal_edit'),
    path('goal/<int:pk>/delete/', GoalDeleteView.as_view(), name='goal_delete'),
    path('goal/', GoalListView.as_view(), name='goal_list'),
    
    # Report URL
    path('report/', ReportView.as_view(), name='report'),
]


