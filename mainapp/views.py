from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from mainapp.forms import AddJobForm, EditJobForm, DeleteJobForm, AddDocForm, EditDocForm, DeleteDocForm, \
    CreateUserForm, EditUserDetailsForm, UserChangePasswordCustom
from mainapp.models import Job, Document


# Register View ########################################################################################################

def registeruser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save()
            newform.is_active = True
            newform.save()

            return redirect('login')
    context = {'form': form, }
    return render(request, 'login/register.html', context)


# Login View ###########################################################################################################
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            loginUsername = request.POST.get('loginUsername')
            loginPassword = request.POST.get('loginPassword')

            user = authenticate(request, username=loginUsername, password=loginPassword)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')

        return render(request, 'login/login.html')


def logoutuser(request):
    logout(request)
    return redirect('login')


# Index View ###########################################################################################################
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


# Profile View #########################################################################################################
@login_required(login_url='login')
def user_profile(request, pid):
    user = User.objects.get(id=pid)
    context = {'user': user}
    return render(request, 'user/profile.html', context)


def edituser(request, pid):
    user = User.objects.get(id=pid)
    form = EditUserDetailsForm(instance=user)

    if request.method == 'POST':
        form = EditUserDetailsForm(request.POST, request.FILES)

        if form.is_valid():
            user_new_info = form.save(commit=False)
            user.first_name = user_new_info.first_name
            user.last_name = user_new_info.last_name
            user.email = user_new_info.email
            user.save()

            return redirect('user_profile', pid)

    context = {'form': form, 'user': user}
    return render(request, 'user/editprofile.html', context)


# CHANGE PASSWORD ######################################################################################################
def changepass(request, pid):
    pid = pid
    user = User.objects.get(id=pid)

    form = UserChangePasswordCustom(user)

    if request.method == 'POST':
        form = UserChangePasswordCustom(user, request.POST)

        if form.is_valid():
            form.save()
            return redirect('user_profile', pid)

    context = {'form': form, 'user': user}
    return render(request, 'user/changepassword.html', context)


# Job View #############################################################################################################
def job(request):
    current_user = request.user.username
    jobObj = Job.objects.filter(user_ref__username=current_user)

    context = {'jobObj': jobObj}
    return render(request, 'job/job.html', context)


def addjob(request):
    form = AddJobForm()

    if request.method == 'POST':
        form = AddJobForm(request.POST, request.FILES)

        if form.is_valid():
            newform = form.save()
            newform.user_ref = request.user
            newform.save()
            return redirect('job')

    context = {'form': form}
    return render(request, 'job/addjob.html', context)


def editjob(request, jid):
    jObj = Job.objects.get(id=jid)
    form = EditJobForm(instance=jObj)

    if request.method == 'POST':
        form = EditJobForm(request.POST, request.FILES)

        if form.is_valid():
            newform = form.save(commit=False)
            jObj.job_name = newform.job_name
            jObj.job_title = newform.job_title
            jObj.job_location = newform.job_location
            jObj.job_ctc = newform.job_ctc
            jObj.job_requirement = newform.job_requirement
            jObj.register_date = newform.register_date
            jObj.register_site = newform.register_site
            jObj.save()
            return redirect('job')

    context = {'form': form}
    return render(request, 'job/editjob.html', context)


def singlejob(request, jid):
    jObj = Job.objects.get(id=jid)

    context = {'jObj': jObj}
    return render(request, 'job/singlejob.html', context)


def deletejob(request, jid):
    jObj = Job.objects.get(id=jid)
    form = DeleteJobForm(initial={'job_name': jObj.job_name})

    if request.method == 'POST':
        form = DeleteJobForm(request.POST, request.FILES)

        if form.is_valid():
            job_name = form.cleaned_data.get('job_name')
            if jObj.job_name == job_name:
                jObj.delete()
                return redirect('job')

    context = {'form': form}
    return render(request, 'job/deletejob.html', context)


# Document View ########################################################################################################
def document(request):
    current_user = request.user.username
    docObj = Document.objects.filter(user_ref__username=current_user)

    context = {'docObj': docObj}
    return render(request, 'document/document.html', context)


def adddoc(request):
    form = AddDocForm()
    if request.method == 'POST':
        form = AddDocForm(request.POST, request.FILES)
        if form.is_valid():
            newform = form.save()
            newform.user_ref = request.user
            newform.save()
            return redirect('document')

    context = {'form': form}
    return render(request, 'document/adddoc.html', context)


def editdoc(request, did):
    dObj = Document.objects.get(id=did)
    form = EditDocForm(instance=dObj)

    if request.method == 'POST':
        form = EditDocForm(request.POST, request.FILES)

        if form.is_valid():
            newform = form.save(commit=False)
            dObj.doc_name = newform.doc_name
            dObj.document_file = newform.document_file
            dObj.save()
            return redirect('document')

    context = {'form': form}
    return render(request, 'document/editdoc.html', context)


def deletedoc(request, did):
    dObj = Document.objects.get(id=did)
    form = DeleteDocForm(initial={'doc_name': dObj.doc_name})

    if request.method == 'POST':
        form = DeleteDocForm(request.POST, request.FILES)

        if form.is_valid():
            doc_name = form.cleaned_data.get('doc_name')
            if dObj.doc_name == doc_name:
                dObj.delete()
                return redirect('document')

    context = {'form': form}
    return render(request, 'document/deletedoc.html', context)
