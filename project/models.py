from django.db import models
from django.utils import timezone


class Project(models.Model):
    foto        = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=300)
    tags        = models.CharField(max_length=100)
    url_github  = models.CharField(max_length=100)
    created_at  = models.DateField(auto_now_add=True)
    class Meta:
        db_table ='Project'

    def completar(self):
        self.created_at= timezone.now()
        return self.save()