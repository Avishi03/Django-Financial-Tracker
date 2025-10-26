from django.urls import path,include 
'''#from . import views
#from finance.views import home, HomeView
urlpatterns = [
    path('home/', home, name="home" ),
    path('', HomeView.as_view(), name="ghar"),
]'''
from finance.views import RegisterView, DashboardView
urlpatterns = [
     path('register/', RegisterView.as_view(), name="register"),
     path('', DashboardView.as_view(), name="dashboard")
]


