import json
import numpy as np
from urllib import request as r
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
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