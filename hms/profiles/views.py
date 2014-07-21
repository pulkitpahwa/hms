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
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, UpdateView, DetailView

from braces.views import LoginRequiredMixin

from .models import Student, StaffUser, HostelStaff
from .forms import StudentCreateForm, StudentUpdateForm


class ProfileActionMixin(object):

    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)
        
    def form_valid(self, form):
        msg = "Profile {0}!".format(self.action)
        messages.info(self.request,msg)
        return super(ProfileActionMixin, self).form_valid(form)
        
#send this form as the first page initially when the user is just registered. If the form is filled, send him to the bootstrap/index.html page.
class StudentCreateView(LoginRequiredMixin, ProfileActionMixin, CreateView):
    
    model = Student
    action = "created"
    template_name = 'profiles/user_form.html'
    form_class = StudentCreateForm


class UserInfoMixin(object):
    def get_context_data(self,**kwargs):
        context = super(UserInfoMixin, self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['userinfo'] = user
        return context



class StudentUpdateView(LoginRequiredMixin, ProfileActionMixin, UserInfoMixin, UpdateView):
    
    model = Student
    action = "created"
    form_class = StudentUpdateForm
    
    def form_valid(self, form):
        user = get_object_or_404(User, username =self.request.user.username)
        form.instance.user = user
        return super(StudentUpdateView, self).form_valid(form)



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

