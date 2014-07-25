from django.contrib import auth
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.core.context_processors import csrf
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context,Template, RequestContext

from profiles.models import Student
from attendance.models import Holidays, Attendance
from outpas.models import Outpass


class StudentCreate(CreateView):
    model = Student

class StudentUpdate(UpdateView):
    model = Student

class StudentList(ListView):
    model = Student

#make this page different on the basis of the whether the user is student,staff or hostel staff
@login_required
def home(request):
    holidays = Holidays.objects.all()[0:10]
    user = Student.objects.get(enrollment_id = request.user).name
    a = get_template("index.html")
    c = Context({'holiday_list':holidays,'name':user})
    html = a.render(c)
    return HttpResponse(html)	


#def staff_permission_received(request):
# if this function gets called, do the following things :
#   1 . Delete all the messages that were sent to all the concerned people
#   2 . set staff_permission_required to false
#   3 . set permission_received_by to the request.user
#   4 . if girls_permission_required = false, then for all dates that lie in between the from_date and return_date, set present = no, absent = no, and outpass = true
#   5 . set outpass_state = P



#def hostel_staff_permission_received(request):
# if this function gets called, do the following things :
#   1 . Delete all the messages that were sent to all the hostel_warden
#   2 . set hostel_staff_permission_required to false
#   3 . set permission_granted_by_hostel_staff to the request.user
#   4 . if staff_permission_required = false, then for all dates that lie in between the from_date and return_date, set present = no, absent = no, and outpass = true
#   5 . set outpass_state = P



def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/profile')
            else:
                # An inactive account was used - no logging in!
                return HttpResponseRedirect("/outpass")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)
        
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
