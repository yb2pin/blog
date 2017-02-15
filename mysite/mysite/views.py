from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    c = Context({'current_date':now})
    html = t.render(c)
    return HttpResponse(html)

def current_datetime2(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    t = get_template('hours_ahead.html')
    html = t.render(Context({'offset': offset, 'dt':dt}))
    return HttpResponse(html)
