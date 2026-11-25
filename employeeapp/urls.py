from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('add-employee',views.add_employee,name='add_employee'),
    path('employee-list/', views.employee_list, name='employee_list'),
]