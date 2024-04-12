from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class FlowType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Classification(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Flow(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    type_of = models.ForeignKey(
        FlowType, on_delete=models.SET_NULL, blank=True, null=True)
    classification = models.ForeignKey(
        Classification, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class CashFlow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(default=timezone.now)
    value = models.FloatField()
    flow = models.ForeignKey(
        Flow, on_delete=models.SET_NULL, blank=True, null=True)
    observation = models.TextField(blank=True)
