from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mv_test.models import Group

def index(request):
    groups = Group.objects.all()
    
    context={
        'groups': groups,
    }
    return render_to_response( 'mv_test/index.html', RequestContext(request, context))

def group(request, gid):
    group = get_object_or_404(Group, pk=gid)
    context={
        'group': group,
    }
    return render_to_response( 'mv_test/group.html', RequestContext(request, context))

#eof
