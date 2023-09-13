from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.
def index(request):
    events=Event.objects.all()
    
    return render(request,'index.html',context = {
        'events' : events 
    })

def eventdetail(request, pk):
    event_single=Event.objects.get(pk=pk)
    context = {
        'event':event_single
    }
    return render(request,'detail1.html',context)
