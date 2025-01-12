from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=15)

class Lapd(models.Model):
    unit = models.CharField(max_length=15)
    no_nd = models.CharField(max_length=15)
    tgl_nd = models.DateField()
    nama = models.CharField(max_length=15)
    nip = models.CharField(max_length=16)
    jabatan = models.CharField(max_length=15)
    jns_data = models.CharField(max_length=15)
    uraian = models.CharField(max_length=15)

    def __str__(self):
        return self.name
