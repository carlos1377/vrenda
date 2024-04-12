from django.contrib import admin
from .models import Flow, Classification, FlowType, CashFlow
# Register your models here.

admin.site.register(Flow)
admin.site.register(Classification)
admin.site.register(FlowType)
admin.site.register(CashFlow)
