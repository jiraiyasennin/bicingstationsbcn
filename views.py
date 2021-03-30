from django.shortcuts import render
from .forms import BicingForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def bicing(request):
    data={}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BicingForm(request.POST)
        #checks if the form has changed to manage the empty fields
        if form.has_changed():
        # check whether it's valid, and then, sends the data to the template
         if form.is_valid():
             lat= form.cleaned_data.get('lat')
             long= form.cleaned_data.get('long')
             data= form.arrayStations(lat,long)
         return render(request, 'dashboard/bicing/stations_around.html', {'data':data})
        else:
         form = BicingForm()
         messages.add_message(request, messages.INFO, f'Debes activar la geolocalización')
         return render(request, 'dashboard/bicing/bicing.html', {'form':form})
    else:
      form = BicingForm()
    return render(request, 'dashboard/bicing/bicing.html', {'form':form})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
