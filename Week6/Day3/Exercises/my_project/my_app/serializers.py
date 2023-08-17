from rest_framework import serializers
from .models import Department, Employee, Project, Task


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def validate_name(self, value):
        if Department.objects.filter(name=value).exists():
            raise serializers.ValidationError("A department with this name already exists.")
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError("A project with this name already exists.")
        return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
