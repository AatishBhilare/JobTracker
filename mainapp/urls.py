from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # USER URLS #######################################################################################################
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('registeruser/', views.registeruser, name='registeruser'),
    # USER PROFILE #####################################################################################################
    path('user-profile/<int:pid>/', views.user_profile, name='user_profile'),
    path('user-profile/edit-user/<int:pid>/', views.edituser, name='edituser'),
    path('user-profile/change-password/<int:pid>/', views.changepass, name='changepass'),
    # JOB URLS #########################################################################################################
    path('job', views.job, name='job'),
    path('job/add', views.addjob, name='addjob'),
    path('job/edit/<int:jid>/', views.editjob, name='editjob'),
    path('job/view/<int:jid>/', views.singlejob, name='singlejob'),
    path('job/<int:jid>/delete', views.deletejob, name='deletejob'),
    # DOCUMENT URLS ####################################################################################################
    path('document', views.document, name='document'),
    path('document/add', views.adddoc, name='adddoc'),
    path('document/edit/<int:did>/', views.editdoc, name='editdoc'),
    path('document/<int:did>/delete', views.deletedoc, name='deletedoc'),
]
