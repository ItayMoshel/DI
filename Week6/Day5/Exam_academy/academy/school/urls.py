from django.urls import path
from .views import CourseDetailsView, TeacherListView, SchoolFacilityListView, LaboratoryListView

urlpatterns = [
    path('course/<int:course_id>/', CourseDetailsView.as_view(), name='course-details'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('facilities/', SchoolFacilityListView.as_view(), name='facility-list'),
    path('labs/', LaboratoryListView.as_view(), name='lab-list'),
]
