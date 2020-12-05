from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexPageView(request):
    return render(request, 'User/profile.html')


'''def addClientFormView(request) :
    form = addClientForms()
    context = {
        'form': form
    }
    return render(request, 'clientview_a/add.html', context)

def addClientView(request) :
    if request.method == 'POST':

    #Create a new employee object from the model (like a new record)
        new_client = Person()
        
        #Store the data from the form to the new object's attributes (like columns)
        new_client.first_name = request.POST.get('first_name')
        new_client.last_name = request.POST.get('last_name')
        new_client.spouse = request.POST.get('spouse')
        new_client.ssn = request.POST.get('ssn')
        new_client.birthdate = request.POST.get('birthdate')
        new_client.occupation = request.POST.get('occupation') 
        new_client.address = request.POST.get('address')
        new_client.city = request.POST.get('city')
        new_client.state = request.POST.get('state')
        new_client.phone = request.POST.get('phone')
        new_client.email = request.POST.get('email')
        
        #Save the employee record
        new_client.save()
    
    #Make a list of all of the employee records and store it to the variable
    data = Person.objects.all()
    
    #Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "clients" : data
    }
    return render(request, 'clientview_a/indexacc.html', context)'''
