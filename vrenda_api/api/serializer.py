from rest_framework import serializers
from .models import Flow, FlowType, CashFlow, Classification


class FlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flow
        fields = '__all__'
