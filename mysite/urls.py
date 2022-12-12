
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path, include
from user.views import Error500View, Error404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('project.urls')),
]
#manejo de errores
handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()