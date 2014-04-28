from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib import auth
from django.template import RequestContext
from kibytci.models import Gismu, Proposal

def ro_gismu(request):
    gimste = Gismu.objects.all()
    for g in gimste:
        g.proposals = Proposal.objects.filter(gismu=g).order_by('klesi')
    return render(request, 'ro_gismu.html',
                  {'gimste': gimste},
                  context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return redirect(str(request.META['HTTP_REFERER']))

