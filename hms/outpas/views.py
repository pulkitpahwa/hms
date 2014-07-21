from django.template import RequestContext
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import modelformset_factory
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.template import Context,Template
from django.template.loader import get_template
# Imports for add-or-edit object form.
# TODO: Fix the experiment-edit form to syntactically resemble the room-edit form.
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

@login_required
def all_outpass(request):
    a = get_template("index.html")
    enrollment_id = request.GET['username']
    c = Context({'user':enrollment_id})
    html = a.render(c)
    return HttpResponse(html)	



@login_required
def my_all_outpass(request):
    a = get_template("index.html")
    enrollment_id = request.GET['username']
    c = Context({'user':enrollment_id})
    html = a.render(c)
    return HttpResponse(html)	

@login_required
def create_outpass(request):
    a = get_template("index.html")
    enrollment_id = request.GET['username']
    c = Context({'user':enrollment_id})
    html = a.render(c)
    return HttpResponse(html)	

@login_required
def update_outpass(request):
    a = get_template("index.html")
    enrollment_id = request.GET['username']
    c = Context({'user':enrollment_id})
    html = a.render(c)
    return HttpResponse(html)	

