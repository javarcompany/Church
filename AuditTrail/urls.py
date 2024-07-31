from django.urls import path #type:ignore
from .views import *

urlpatterns = [
    path('system/audits/', view_audits, name='view_audits'),
]