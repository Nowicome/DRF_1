from django.urls import path
from measurement.views import ListSensorAPIView, StatusSensorAPIView, MeasurementsAddAPIView

urlpatterns = [
    path("sensors/", ListSensorAPIView.as_view()),
    path("sensors/<int:pk>/", StatusSensorAPIView.as_view()),
    path("measurements/", MeasurementsAddAPIView.as_view()),
]
