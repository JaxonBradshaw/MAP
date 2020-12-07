from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ApplicantUserForm, OrgAdminUserForm
from .models import Applicant, Organization_Admin, Person
from django.contrib.auth import authenticate, login

# Create your views here.

def indexPageView(request):
    return render(request, 'User/profile.html')

def choiceView(request):
    return render(request, 'User/choice.html')  

def register_applicantView(request) :
    form = ApplicantUserForm(request.POST or None)
    if request.method == 'POST' :
        form = ApplicantUserForm(request.POST)
        if form.is_valid() :
            #form.type = "Applicant" add later
            form.save()
            return redirect('/account/login')
    context = {
        'form': form
    }
    return render(request, 'User/register/applicant.html', context)

def register_org_adminView(request) :
    form = OrgAdminUserForm(request.POST or None)
    if request.method == 'POST' :
        form = OrgAdminUserForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/account/login')
    context = {
        'form': form
    }
    return render(request, 'User/register/org_admin.html', context)

def profileView(request) :
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    person = Person.objects.get(username=username)
    if user is not None:
        if person.type=='applicant':
            applicant = Applicant.objects.get(id = user.id)
            context = {
                'user' : applicant,
            }
        else:
            orgadmin = Organization_Admin.objects.get(id = user.id)
            context = {
                'user' : orgadmin,
            }
        login(request, user)
        
        return render(request, 'User/profile.html', context)
    else:
        return redirect('/account/login')

def viewApplicantsView(request):
    data = Applicant.objects.all()
    context = {
        "applicant" : data
    }
    return render(request, 'User/applicants.html', context)

def viewOrgAdminView(request):
    data = Organization_Admin.objects.all()

    context = {
        "orgadmin" : data
    }
    return render(request, 'User/orgadmins.html', context)