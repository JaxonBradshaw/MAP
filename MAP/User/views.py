import json
import numpy as np
from urllib import request as r
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ApplicantUserForm, OrgAdminUserForm
from .models import Applicant, Organization_Admin, Person
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def indexPageView(request):
    return render(request, 'User/profile.html')

def choiceView(request):
    return render(request, 'User/choice.html')  
# use this thingy
def register_applicantView(request) :
    form = ApplicantUserForm(request.POST or None)
    if request.method == 'POST' :
        form = ApplicantUserForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/account/login')
    context = {
        'form': form
    }
    return render(request, 'User/register/applicant.html', context)
# or this thingy
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
    currentuser = request.user
    user = authenticate(request, credentials=currentuser)   
    if request.method == 'POST' :
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
    person = Person.objects.get(username=currentuser.username)
    if person.type=='applicant':
        applicant = Applicant.objects.get(id = currentuser.id)
        context = {
            'user' : applicant,
        }
    else:
        orgadmin = Organization_Admin.objects.get(id = currentuser.id)
        context = {
            'user' : orgadmin,
        }
    
    context = {
        'user' : person,
    }  
    return render(request, 'User/profile.html', context)

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

def viewDreamJobView(request):
    return render(request, 'User/dream_job.html')

def dreamJobView(request):
 # Convert JSON byte stream into dictionary

    data =  {
            "Inputs": {
                    "input1":
                    {
                        "ColumnNames": ["job_title"],
                        "Values": [[
            request.GET['reviewerID'],
            ]]
                    },
            },
        }
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/e52f975d4320488386b8c05bc82f2238/services/0584b765f93b40b8844598279faf5ee8/execute?api-version=2.0&details=true'
    api_key = 'H9hsb8o+KykvXyeD6QvqUiMO44tx8kBR2wunZBGr1nSSu0pFESUjM5k+FtXtDARaedqjEnakmAnCnOj1t+qy6g==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    #Generate web service request
    req =r.Request(url, body, headers)
    req.method = "POST"
    response = r.urlopen(req)
    result = response.read()
    result = json.loads(result)
    prediction = result['Results']['output1']['value']['Values'][0]

    data = {'matchbox_results':str(f'1. {prediction[0]}, 2.{prediction[1]}, 3.{prediction[2]}, 4.{prediction[3]}, 5.{prediction[4]}')}

    return render(request, 'User/dream_job.html', data)

def logoutrequestView(request) :
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("registration/login.html")


def editprofileView(request) :
    currentuser = request.user
    user = authenticate(request, credentials=currentuser)   
    person = Person.objects.get(username=currentuser.username)
    if request.method == 'POST' :   
        if person.type=='applicant':
            form = ApplicantUserForm(request.POST)
            if form.is_valid():
                form.save()
                applicant = Applicant.objects.get(id = user.id)
                context = {
                    'user' : applicant,
                }
                #return render(request, 'User/profile.html', context)
                return HttpResponse('1')
        else:
            form = OrgAdminUserForm(request.POST)
            if form.is_valid():
                form.save()
                orgadmin = Organization_Admin.objects.get(id = user.id)
                context = {
                    'user' : orgadmin,
                }
                #return render(request, 'User/profile.html', context)
                return HttpResponse('2')
        return HttpResponse('3')
    context = {
        'user' : person,
    }  
    #return render(request, 'User/editprofile.html', context)
    return HttpResponse('4')