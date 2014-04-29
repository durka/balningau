from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib import auth
from django.template import RequestContext
from django_comments.models import Comment
from kibytci.models import User, Gismu, Proposal

def ro_gismu(request):
    gimste = Gismu.objects.all()
    for g in gimste:
        g.proposals = Proposal.objects.filter(gismu=g).order_by('klesi')
    return render(request, 'ro_gismu.html',
                  {'gimste': gimste},
                  context_instance=RequestContext(request))

def selstidi(request, id):
    return render(request, 'selstidi.html',
                   {'selstidi': Proposal.objects.get(id=id)},
                   context_instance=RequestContext(request))

def pinka_cikre(request, id):
    comment = Comment.objects.get(id=id)
    comment.comment = request.POST['comment']
    comment.save()
    return redirect('comments-comment-done')

def logout(request):
    auth.logout(request)
    return redirect(str(request.META['HTTP_REFERER']))

def new_user(request):
    user = User.objects.create_user(request.POST['username'],
                                    password=request.POST['password'],
                                    email=request.POST['email'],
                                    first_name=request.POST['fullname'])
    user.save()
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    auth.login(request, user)
    return redirect(request.POST['next'])

