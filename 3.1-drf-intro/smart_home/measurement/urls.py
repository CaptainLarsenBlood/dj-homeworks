from django.urls import path

from measurement.views import SensorsAPIList, MeasurementAPIList, SensorAPIDetail

urlpatterns = [
    path('sensors/', SensorsAPIList.as_view()),
    path('measurements/', MeasurementAPIList.as_view()),
    path('sensors/<pk>/', SensorAPIDetail.as_view()),
]
