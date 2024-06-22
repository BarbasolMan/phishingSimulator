from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhishingEmailTemplateForm
from .models import PhishingEmailTemplate

# Create your views here.
def create_tempalte(request):
    if request.method == 'POST':
        form = PhishingEmailTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            attachment = form.cleaned_data.get('attachment')
            
            # Create a new PhishingEmailTemplate instance and save it
            PhishingEmailTemplate.objects.create(subject=subject, body=body, attachment=attachment)
            
            return redirect('success')
    else:
        form = PhishingEmailTemplateForm()
    
    return render(request, 'phishTemplates/create_template.html', {'form': form})

def templateHome(request):
    templates = PhishingEmailTemplate.objects.all()
    return render(request, 'phishTemplates/template_list.html', {'templates': templates})