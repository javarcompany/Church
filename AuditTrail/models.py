from django.db import models #type:ignore
from django.contrib.auth.models import User #type:ignore

class AuditTrail(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    action=models.CharField(max_length=2000)
    page=models.CharField(max_length=2000,blank=True, null=True)
    ipaddress=models.GenericIPAddressField(max_length=2000)
    computer = models.CharField(max_length=2000)
    dot=models.DateTimeField(verbose_name='Date of Trail', auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return  str(self.user) +' '+ self.action

    class Meta:
            verbose_name = ('Audit Trail')
            verbose_name_plural = ('Audits Trails' )