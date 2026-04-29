# from ast import Import
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, CourseViewSet, EnrollmentViewSet
router = DefaultRouter()

# router.register('customer', CustomerViewSets, basename='customer')
# router.register('ministerialPublication', MinisterialPublicationViewSets, basename='ministerialPublication')
# router.register('complaint', ComplaintViewSets, basename='complaint')

router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('enrollments', EnrollmentViewSet)

urlpatterns = [
path('api/', include(router.urls)),


# path('send/<str:customerName>/<str:phoneNumber>/<str:subject>', send, name="send"),
# path('send/<str:customerName>/<str:phoneNumber>/<str:subject>', send, name="send"),
# path('sendwithproducts/', sendProductsDetails, name="sendwithproducts")





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)