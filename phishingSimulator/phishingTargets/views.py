from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def phishingTarget(request):
    return render(request, 'phishingTargets/targetsMain.html')