from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import HostsForm
from .models import Hosts, User


@login_required
def index(request):
    if request.user.is_staff:
        hosts = Hosts.objects.all()
    else:
        username = request.user.username
        owner = get_object_or_404(User, username=username)
        hosts = owner.hosts.all()
    context = {
        'hosts': hosts,
    }
    return render(request, 'index.html', context)


@login_required
def hosts_create(request):
    form = HostsForm(request.POST or None)
    if form.is_valid():
        hosts = form.save(commit=False)
        hosts.owner = request.user
        hosts = form.save()
        return redirect('hosts:index')
    return render(request, 'hosts_create.html', {'form': form})


@login_required
def hosts_edit(request, hosts_id):
    hosts = get_object_or_404(Hosts, id=hosts_id)
    is_edit = True
    if (hosts.owner != request.user) and (request.user.is_staff is not True):
        return redirect('hosts:index')
    form = HostsForm(
        request.POST or None,
        instance=hosts
    )
    if form.is_valid():
        form.save()
        return redirect('hosts:index')
    context = {
        'hosts': hosts,
        'form': form,
        'is_edit': is_edit
    }
    return render(request, 'hosts_create.html', context)
