from django import forms

class ProjectForm(forms.Form):
    foto        = forms.CharField(max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea())
    tags        = forms.CharField(max_length=100)
    url_github  = forms.CharField(max_length=100)