from ipware import get_client_ip
from .models import IpClient
def ip_is_valid(get_response):

    def middleware(request):
        ip, is_routable = get_client_ip(request)
        IpClient.objects.create(ip=ip)
        return get_response(request)

    return middleware