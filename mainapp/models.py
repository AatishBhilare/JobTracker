from django.contrib.auth.models import User
from django.db import models


# Job Model ############################################################################################################
class Job(models.Model):
    user_ref = models.ForeignKey(User, models.SET_NULL, verbose_name='user_ref', null=True)
    job_name = models.CharField(verbose_name='JobName', max_length=255)
    job_title = models.CharField(verbose_name='JobTitle', max_length=255)
    job_location = models.CharField(verbose_name='JobLocation', max_length=255)
    job_ctc = models.IntegerField(null=True)
    job_requirement = models.TextField(verbose_name='JobRequirement', max_length=20000)
    register_date = models.DateField(verbose_name='RegisterDate', blank=True, null=True)
    register_site = models.CharField(verbose_name='RegisterSite', max_length=255)


# Document Model #######################################################################################################
class Document(models.Model):
    user_ref = models.ForeignKey(User, models.SET_NULL, verbose_name='user_ref', null=True)
    doc_name = models.CharField(verbose_name='DocName', max_length=255)
    document_file = models.FileField(upload_to='documents/')
