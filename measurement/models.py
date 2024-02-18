from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Температура")
    measurement_time = models.DateTimeField(auto_now_add=True, verbose_name="Время измерения")
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
