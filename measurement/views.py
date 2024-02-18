from django.shortcuts import render
from rest_framework import generics, permissions

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementAddSerializer


class ListSensorAPIView(generics.ListCreateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()
    permission_classes = [permissions.AllowAny]


class StatusSensorAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()
    permission_classes = [permissions.AllowAny]


class MeasurementsAddAPIView(generics.CreateAPIView):
    serializer_class = MeasurementAddSerializer
    queryset = Measurement.objects.all()
    permission_classes = [permissions.AllowAny]
