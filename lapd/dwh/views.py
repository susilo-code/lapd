from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City,Lapd
import pandas as pd
from datetime import datetime
from .forms import LapdForm
# Create your views here.

def index(request):
	cities = City.objects.all() 
	return render(request, 'index.html', {'cities': cities})

def lapd_entry(request):
    if request.method == 'POST':
        unit = request.POST.get('unit')
        no_nd = request.POST.get('no_nd')
        tgl_nd = request.POST.get('tgl_nd')
        nama = request.POST.get('nama')
        nip = request.POST.get('nip')
        jabatan = request.POST.get('jabatan')
        jns_data = request.POST.get('jns_data')
        uraian = request.POST.get('uraian')
        lapd = Lapd(unit=unit, no_nd=no_nd, tgl_nd=tgl_nd, nama=nama, nip=nip, jabatan=jabatan, jns_data=jns_data, uraian=uraian)
        lapd.save()
        return redirect('generate')
    else:
        return HttpResponse("Invalid request method.")


def generate(request):
    datas = Lapd.objects.all()
    return render(request, 'generate.html', {'datas':datas})



	
	