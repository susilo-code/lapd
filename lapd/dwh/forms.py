from django import forms

# creating a form
class LapdForm(forms.Form):
    unit = forms.CharField()
    no_nd = forms.CharField() 
    tgl_nd = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    nama = forms.CharField()
    nip = forms.CharField(max_length=16)
    jabatan = forms.CharField()
    jns_data = forms.CharField()
    uraian  = forms.CharField()