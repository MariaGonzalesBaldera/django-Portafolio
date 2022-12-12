from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from .forms import ProjectForm
from .models import Project
# Create your views here.

class AddProject(FormView):
    model = Project
    form_class = ProjectForm
    template_name ='formProject.html'
    def form_valid(self,form):
        Project.objects.create(**form.cleaned_data)
        return redirect('index')

class ListProject(ListView):
    model = Project
    template_name = 'index.html'
    