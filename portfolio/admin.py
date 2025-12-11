from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Certificate)
admin.site.register(models.Contact)
admin.site.register(models.Project)
admin.site.register(models.Resume)
admin.site.register(models.Skill)
