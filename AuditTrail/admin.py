from django.contrib import admin
from .models import *

@admin.register(AuditTrail)
class AuditTrailAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'page', 'ipaddress', 'computer', 'dot')
