from django.contrib import admin
from .models import Caller, Patient

# Register your models here.
admin.site.register(Caller)
admin.site.register(Patient)