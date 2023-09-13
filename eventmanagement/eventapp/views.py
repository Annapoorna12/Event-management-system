from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import ApplicantForm


# Create your views here.
def index(request):
    events=Event.objects.all()
    
    return render(request,'index.html',context = {
        'events' : events 
    })

def eventdetail(request, pk):


    event_single=Event.objects.get(pk=pk)
    form = ApplicantForm()
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.event=event_single
            applicant.save()
    context = {
        'event':event_single,
        'form' :form
    }
    return render(request,'detail1.html',context)