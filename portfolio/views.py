from django.shortcuts import render, redirect

# Create your views here.
from .models import Certificate, Skill, Resume, Contact, Project, About
from .forms import ContactForm

def home(request):
    skills= Skill.objects.all()
    projects= Project.objects.all()
    resume= Resume.objects.all()
    about=About.objects.all()
    return render(request, "portfolio/home.html", {
        "skills": skills,
        "project": projects,
        "resume": resume,
        "about":about,
    })
    
def certificates_view(request):
    certificates= Certificate.objects.all()
    return render(request, "portfolio/certificates.html", {"certificates":certificates})

def contact_me(request):
    if request.method=="POST":
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
        else:
            form= ContactForm()
    return render(request, "portfolio/contact.html", {"form":form})    
    
        