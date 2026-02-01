from django.contrib import admin
from .models import Transaction, Goal

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount', 'transaction_type', 'category', 'date')
    list_filter = ('transaction_type', 'category', 'date', 'user')
    search_fields = ('title', 'category', 'user__username')
    date_hierarchy = 'date'
    ordering = ('-date', '-id')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'target_amount', 'deadline')
    list_filter = ('deadline', 'user')
    search_fields = ('name', 'user__username')
    date_hierarchy = 'deadline'
    ordering = ('deadline',)