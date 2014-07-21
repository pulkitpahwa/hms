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


from .models import Student, StaffUser, HostelStaff


@login_required
def view_profile(request):  
    try:
        Student.objects.get(enrollment_id = request.user)
        enrollment_id = Student.objects.get(enrollment_id = request.user)
        a = get_template("profiles/students_index.html")
        c = Context({'name':enrollment_id, 'edit':"<li><a href = 'edit'>Edit Profile</a></li>"})
    except:
        try:
            StaffUser.objects.get(enrollment_id = request.user)
            enrollment_id = StaffUser.objects.get(enrollment_id = request.user)
            a = get_template("profiles/staff_index.html")
            c = Context({'name':enrollment_id, 'edit':"<li><a href = 'edit'>Edit Profile</a></li>"})
        except:
            try:
                enrollment_id = HostelStaff.objects.get(enrollment_id = request.user)
                a = get_template("profiles/hostelstaff_index.html")
                c = Context({'name':enrollment_id, 'edit':"<li><a href = 'edit'>Edit Profile</a></li>"})
            except:
                return HttpResponse("You don't have enough permissions to access the login panel.<a href = '/logout'>Logout</a>")
    html = a.render(c)
    return HttpResponse(html)	


@login_required
def edit_profile(request):
    a = get_template("index.html")
    enrollment_id = request.user
    c = Context({'user':enrollment_id})
    html = a.render(c)
    return HttpResponse(html)	

