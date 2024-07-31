from django.shortcuts import render, redirect #type:ignore
from django.contrib.auth.decorators import login_required   #type:ignore

from .models import *
from Index.variables import context

def audit(request, action = None):
    
    ipaddress = request.META.get('HTTP_X_FORWARDED_FOR')
    if ipaddress:
        ipaddress = ipaddress.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')

    audit = AuditTrail(user = request.user, action = action, page=request.META.get('HTTP_REFERER'), ipaddress = ipaddress,
                        computer = request.headers['User-Agent'])
    audit.save()
                

@login_required(login_url = 'login')
def view_audits(request):
    if request.user.is_superuser:
        audits = AuditTrail.objects.all()
        context["Audits"] = audits
        return render(request, "audittrail/view_audits.html", context)
    else:
        return redirect('index')
