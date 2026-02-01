from django.urls import path,include 
'''#from . import views
#from finance.views import home, HomeView
urlpatterns = [
    path('home/', home, name="home" ),
    path('', HomeView.as_view(), name="ghar"),
]'''
from finance.views import RegisterView, DashboardView, TransactionCreateView, TransactionListView
urlpatterns = [
     path('register/', RegisterView.as_view(), name="register"),
     path('', DashboardView.as_view(), name="dashboard"),
     path('tansaction/add/', TransactionCreateView.as_view(),name='transaction_add'),
     path('tansaction/', TransactionListView.as_view(),name='transaction_list'),
]


