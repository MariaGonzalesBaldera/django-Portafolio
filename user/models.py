from django.db import models

from django.db import models
from django.utils import timezone


class Project(models.Model):
    nombre        = models.CharField(max_length=200, default='Nombre del proyecto')
    foto        = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=300)
    tags        = models.CharField(max_length=100)
    url_github  = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table ='Projects'

    def completar(self):
        self.created_at= timezone.now()
        return self.save()

class IpClient(models.Model):
    ip = models.CharField(max_length=30)
    created_at  = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table ='IpClient'

    def completar(self):
        self.created_at= timezone.now()
        return self.save()