from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import Textarea, TextInput, DateInput, FileInput, PasswordInput, EmailInput, CharField

from mainapp.models import Job, Document


# USER FORM ############################################################################################################
class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={}))
    password1 = forms.CharField(widget=PasswordInput(attrs={}))
    password2 = forms.CharField(widget=PasswordInput(attrs={}))

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password', 'date_joined']


class EditUserDetailsForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {

            "first_name": TextInput(
                attrs={
                    "class": "form-control"
                }),
            "last_name": TextInput(
                attrs={
                    "class": "form-control"
                }),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "type": "email"
                }),
        }


# CHANGE PASSWORD FORM #################################################################################################
class UserChangePasswordCustom(SetPasswordForm):
    new_password1 = CharField(required=True, label='newpassword',
                              widget=PasswordInput(attrs={
                                  'class': 'form-control'}),
                              error_messages={
                                  'required': 'The password can not be empty'})
    new_password2 = CharField(required=True, label='confirmpassword',
                              widget=PasswordInput(attrs={
                                  'class': 'form-control'}),
                              error_messages={
                                  'required': 'The password can not be empty'})


# JOB FORM #############################################################################################################
class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job

        fields = ['job_name', 'job_title', 'job_location', 'job_ctc', 'job_requirement',
                  'register_date', 'register_site']

        widgets = {
            "job_name": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_title": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_location": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_ctc": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_requirement": Textarea(
                attrs={
                    "class": "form-control"
                }),

            "register_site": TextInput(
                attrs={
                    "class": "form-control"
                }),

        }


class EditJobForm(forms.ModelForm):
    class Meta:
        model = Job

        fields = ['job_name', 'job_title', 'job_location', 'job_ctc', 'job_requirement',
                  'register_date', 'register_site']

        widgets = {
            "job_name": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_title": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_location": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_ctc": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "job_requirement": Textarea(
                attrs={
                    "class": "form-control", 'rows': 2, 'cols': 80
                }
            ),

            "register_site": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "register_date": DateInput(
                attrs={
                    "class": "form-control", 'type': 'date'
                }),

        }


class DeleteJobForm(forms.Form):
    job_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'readonly': True}))


# DOCUMENT FORM ########################################################################################################
class AddDocForm(forms.ModelForm):
    class Meta:
        model = Document

        fields = ['doc_name', 'document_file']

        widgets = {
            "doc_name": TextInput(
                attrs={
                    "class": "form-control"
                }),

            "document_file": FileInput(
                attrs={
                    "class": "form-control-file"
                }),
        }


class EditDocForm(forms.ModelForm):
    class Meta:
        model = Document

        fields = ['doc_name', 'document_file']

        widgets = {
            "doc_name": TextInput(
                attrs={
                    "class": "form-control"
                }),
        }

    def clean_document_file(self):
        document_file = self.cleaned_data['document_file']
        if document_file:
            return document_file
        else:
            document_file = 'emptyfile'
            return document_file


class DeleteDocForm(forms.Form):
    doc_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'readonly': True}))
