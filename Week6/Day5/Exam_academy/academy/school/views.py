from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Teacher, SchoolFacility, Laboratory
from .serializers import CourseSerializer, TeacherSerializer, SchoolFacilitySerializer, LaboratorySerializer


class CourseDetailsView(APIView):
    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
            serialized_course = CourseSerializer(course)
            return Response(serialized_course.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serialized_teachers = TeacherSerializer(teachers, many=True)
        return Response(serialized_teachers.data)


class SchoolFacilityListView(APIView):
    def get(self, request):
        facilities = SchoolFacility.objects.all()
        serialized_facilities = SchoolFacilitySerializer(facilities, many=True)
        return Response(serialized_facilities.data)


class LaboratoryListView(APIView):
    def get(self, request):
        laboratories = Laboratory.objects.all()
        serialized_labs = LaboratorySerializer(laboratories, many=True)
        return Response(serialized_labs.data)
