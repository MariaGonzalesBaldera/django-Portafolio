from django.shortcuts import redirect, render
from django.views.generic import CreateView,FormView,TemplateView, ListView
from django.views.generic.edit import UpdateView
from .forms import NewUserForm, ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Project , IpClient 


class index(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        ListProjects = Project.objects.all()
        ListIPs = IpClient.objects.all()
        return {'ListProjects': ListProjects, 'ListIPs': ListIPs}
        
class ListPaginacion(ListView):
    model = IpClient
    template_name = 'ListIp.html'
    paginate_by = 5
    context_object_name = 'ips'
    
@login_required
def pro_details(request, id):
    print(id)
    project1 = Project.objects.get(id=id)
    print(project1)
    return render(request,'project/portfolio-details.html', {
        'project' : project1
        })

class registerView(CreateView):
    template_name = 'registration/register.html'
    form_class    = NewUserForm
    def form_valid(self, form):
        form.save()
        return redirect('login')
# project
class AddProject(LoginRequiredMixin,FormView):
    model = Project
    form_class = ProjectForm
    template_name ='project/formProject.html'
    def form_valid(self,form):
        Project.objects.create(**form.cleaned_data)
        return redirect('index')

@login_required
def success(request):
   return render(request,'index.html')

class ProjectUpdate(LoginRequiredMixin,UpdateView):
   model=Project
   fields="__all__"
   template_name='project/updateProject.html'
   success_url= '/'


class Error404View(TemplateView):
    template_name = 'errores/error_404.html'


class Error500View(TemplateView):
    template_name = 'errores/error_500.html'
    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view    







