from django.shortcuts import render,HttpResponse
from home.models import contactus
from datetime import datetime
from django.http import HttpResponse
from django.core.management import call_command

def run_migrations(request):
    call_command('makemigrations')
    call_command('migrate')
    return HttpResponse("Migrations Done 🚬💪")



def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')


from django.shortcuts import render, redirect

from django.shortcuts import render, redirect


def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        project=request.POST.get('project')
        name=request.POST.get('name')
        query_description=request.POST.get('query_description')
        
        
        contact=contactus(name=name,email=email,number=number,project=project,query_description=query_description,date=datetime.now())
        contact.save()
    
        
        
      
    
    return render(request, 'contactus.html')



        
        
   


def face_recognition_view(request):
    return render(request, 'face.html')

def virtual_ai_view(request):
    return render(request, 'virtualai.html')

def stock_data_view(request):
    return render(request, 'stockdata.html')

def resume_showcase_view(request):
    return render(request, 'resume.html')

def disease_detection_view(request):
    return render(request, 'diseasedetection.html')

def youtube_instagram_scraper_view(request):
    return render(request, 'youtube_instagram_scraper.html')

# Add other view functions as needed


# Add other view functions as needed



def success(request):
    return render(request, 'success.html')  # This renders a template called success.html






    
