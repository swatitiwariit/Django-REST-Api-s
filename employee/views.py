from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (api_view)
from employee.models import Employee, Designation

# Create your views here.
from employee.serializer import EmployeeSerializer, DesignationSerializer


'''
Author: Swati Tiwari
Date: 14 Mar 2021
Function: Add designation to the database table
Input Params: title, salary (json format)
API URL: http://127.0.0.1:8000/employees/add_designation/
'''
@api_view(['POST'])
def add_designation(request):
    if request.method == "POST":
        saveserializer = DesignationSerializer(data=request.data)
        if saveserializer.is_valid():
            saveserializer.save()
        return Response({"code": 200, "message": "Designation saved successfully", "data": saveserializer.data})
    return Response(status=status.HTTP_400_BAD_REQUEST)


'''
Author: Swati Tiwari
Date: 14 Mar 2021
Function: Add employee to the database table
Input Params: fullname, email, mobile, designation (int) in json format
API URL: http://127.0.0.1:8000/employees/add/
'''
@api_view(['POST'])
def add_employee(request):
    if request.method == 'POST':
        saveserializer = EmployeeSerializer(data=request.data)
        if saveserializer.is_valid():
            saveserializer.save()
        return Response({"code": 200, "message": "Employee saved successfully", "data": saveserializer.data})
    return Response(status=status.HTTP_400_BAD_REQUEST)


'''
Author: Swati Tiwari
Date: 14 Mar 2021
Function: Get all the records from the Employee table 
Input Params: Not required
API URL: http://127.0.0.1:8000/employees/list/
'''
@api_view(['GET'])
def list_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.filter(is_deleted=0).order_by('updated_at')
        data = []
        for emp in employees:
            get_salary = Designation.objects.get(id=emp.designation.id)
            data.append({
                'id': emp.id,
                'fullname': emp.fullname,
                'email': emp.email,
                'mobile': emp.mobile,
                'designation': get_salary.title,
                'salary': get_salary.salary,
            })
        return Response({"code": 200, "message": "User already exists", "data": data})
    return Response(status=status.HTTP_400_BAD_REQUEST)


'''
Author: Swati Tiwari
Date: 14 Mar 2021
Function: Update Employee record
Input Params: id, fullname, email, mobile, designation (int) in json format
API URL: http://127.0.0.1:8000/employees/update/
'''
@api_view(['PATCH'])
def update_employee(request):
    if request.method == 'PATCH':
        emp = Employee.objects.get(pk=request.data['id'])
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            update_emp = serializer.save()
            get_salary = Designation.objects.get(id=update_emp.designation.id)
            data = {
                'id': update_emp.id,
                'fullname': update_emp.fullname,
                'email': update_emp.email,
                'mobile': update_emp.mobile,
                'designation': get_salary.title,
                'salary': get_salary.salary,
            }
        return Response({"code": 200, "message": "Employee updated successfully", "data": data})
    return Response(status=status.HTTP_400_BAD_REQUEST)


'''
Author: Swati Tiwari
Date: 14 Mar 2021
Function: To delete the record from the table, it will not actually delete but set the is_deleted flag to true
Input Params: id, is_deleted (json format)
API URL: http://127.0.0.1:8000/employees/delete/
'''
@api_view(['DELETE'])
def delete_employee(request):
    if request.method == 'DELETE':
        emp = Employee.objects.get(pk=request.data['id'])
        serializer = EmployeeSerializer(emp, data=request.data, partial=True)
        if serializer.is_valid():
            update_emp = serializer.save()   # We can implement delete functionality also instead of update
            data = {
                'id': update_emp.id,
                'fullname': update_emp.fullname,
                'email': update_emp.email,
                'mobile': update_emp.mobile,
                'designation': update_emp.designation.id
            }
        return Response({"code": 200, "message": "Employee updated successfully", "data": data})
    return Response(status=status.HTTP_400_BAD_REQUEST)