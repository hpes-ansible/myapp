import socket

from django.shortcuts import render


def host(request):
    return render(request, 'host/index.html', {
        'host': socket.gethostname(),
    })
