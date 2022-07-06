from django.shortcuts import render
from .models import Hosts
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    hosts = Hosts.objects.order_by('-date')[:10]
    context = {
        'hosts': hosts,
    }
    return render(request, 'index.html', context)
