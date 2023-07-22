# app/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, ClassViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'enrollments', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
