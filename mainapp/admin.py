from django.contrib import admin

# Register your models here.
from mainapp.models import Job, Document

admin.site.register(Job)
admin.site.register(Document)