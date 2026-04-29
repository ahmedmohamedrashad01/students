from django.shortcuts import render
from rest_framework import viewsets, filters, pagination


# import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters


from accounts.models import UserAccount
from accounts.serializers import UserCreateserializer

# from rest_framework.authentication import TokenAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


# Create your views here.
# class ProductPagination(pagination.PageNumberPagination):
#     page_size = 8
#     page_size_query_param = 'page_size'
#     max_page_size = 1000
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateTimeFilter

from rest_framework.viewsets import ModelViewSet

from .models import Student, Course,Enrollment
from .serializers import StudentSerializer,CourseSerializer ,EnrollmentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    
class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer