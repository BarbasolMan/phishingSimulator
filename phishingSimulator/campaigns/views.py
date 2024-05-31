from django.shortcuts import render

# Create your views here.
def campaigns(request):
    return render(request, 'campaigns/campaignsMain.html')