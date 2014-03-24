from django.shortcuts import render
from kibytci.models import Gismu, Proposal
from markdown import markdown

def ro_gismu(request):
    gimste = Gismu.objects.all()
    for g in gimste:
        g.proposals = Proposal.objects.filter(gismu=g).order_by('klesi')
        for p in g.proposals:
            p.velcki = markdown(p.velcki)
    return render(request, 'ro_gismu.html',
                  {'gimste': gimste})

