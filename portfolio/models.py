from django.db import models

# Create your models here.
class Skill(models.Model):
    name= models.CharField(max_length=225)
    level= models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    title= models.CharField(max_length=255)
    github_link= models.URLField(blank=True)
    description= models.TextField()
    languages= models.ManyToManyField(Skill, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    def __str__(self):
        return self.title
        
class Resume(models.Model):
    full_name= models.CharField(max_length=100)
    email= models.EmailField()
    phone_number= models.CharField(max_length=20)
    resume_file= models.FileField(upload_to="resumes/", blank=True)  
    
class Contact(models.Model):
    name= models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    created_time= models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return f"you got message from {self.name}"      
    
class Certificate(models.Model):
    name= models.CharField(max_length=255)
    issued_by= models.CharField(max_length=255)
    skill=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    