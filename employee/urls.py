from django.urls import path
from employee import views

urlpatterns = [
    path('add_designation/', views.add_designation),  # for adding the designation
    path('add/', views.add_employee),                 # for adding the employee
    path('list/', views.list_employees),              # for listing all the employees
    path('update/', views.update_employee),           # for updating employee's record
    path('delete/', views.delete_employee),           # for deleting the employee
]