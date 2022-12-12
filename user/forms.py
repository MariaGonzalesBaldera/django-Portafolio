from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username','first_name' ,'last_name','email','password1','password2')
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user   

# project
texto=forms.TextInput(attrs={'class':'form-control mb-3'})
class ProjectForm(forms.Form):
    nombre        = forms.CharField(max_length=200, widget = texto)
    foto        = forms.CharField(max_length=200, widget = texto)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    tags        = forms.CharField(max_length=100, widget = texto)
    url_github  = forms.CharField(max_length=100, widget = texto)