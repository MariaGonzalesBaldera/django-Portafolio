from ipware import get_client_ip
from .models import IpClient
from django.contrib.auth.models import User


def ip_is_valid(get_response):

    def middleware(request):
        ip, is_routable = get_client_ip(request)
        if request.user.is_authenticated:
            IpClient.objects.create(ip=ip)
        return get_response(request)

    return middleware    