from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_email(self, value):
        existing_student = Student.objects.filter(email=value).first()
        if existing_student:
            raise serializers.ValidationError("A student with this email already exists.")
        return value
