from rest_framework import serializers
from employee.models import Employee, Designation

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ('fullname', 'email', 'mobile', 'designation')
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'