__author__ = 'sam'
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    if FrontPage.objects.count() > 0:

        fp = FrontPage.objects.all()[0]
        if fp.is_video:
            obj = FilmType.objects.filter(is_public=True)
        elif fp.is_image:
            obj = ImageType.objects.filter(is_public=True)
        elif fp.is_audio:
            obj = AudioType.objects.filter(is_public=True)
        context = {
            'obj': obj,
            'fp':fp
        }
        return render_to_response('index.html', context, context_instance=RequestContext(request))
    else:
        raise Http404