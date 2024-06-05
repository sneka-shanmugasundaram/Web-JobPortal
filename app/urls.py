from django.urls import path 
from app import views
from django.contrib import admin
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('admin/', admin.site.urls,),
    path('',views.home , name='jobs_home'),
    path('jobs/',views.jobs , name='jobs'),
    path('job/<int:id>',views.view , name='view'),
    path('apply/<int:id>',views.applyPage,name='apply'),
    path('accounts/register/',views.register ,name='register'),
    path('company_home',views.company_home,name='company_home'),
    path('r_company',views.company_signup,name='r_company'),
    path('l_company/',views.company_login,name='l_company'),
    path('all_applicants/',views.all_applicants,name='all_applicants'),
    path('applicants/<int:id>/',views.applicants,name='applicants'),
    path('logout/', views.logout, name='logout'),
    path('post/',views.postform,name='post'),
    path('update/<int:id>',views.updateform,name='update'),
    path('close/<int:id>',views.closeform,name='close'),
    path('info/<int:id>',views.infoform,name='info'),
    path('location/',views.locationform,name='location'),
    path('author/',views.authorform,name='author'),
    path('skill/',views.skillform,name='skill'),
    path('saveform/',views.saveform,name='saveform'),
    path('profile/',views.profileform,name='profile'),
    path('upform/<int:id>',views.upform,name='upform'),
    path('tenth/<int:id>',views.tenthform,name='tenth'),
    path('p1/<int:id>',views.profile_view,name='p1'),
    path('user/<int:id>',views.profile_view,name='user'),
    path('activate(?p<uidb64>[0-9a-za-z_\-]+)/(?p<token>[0-9a-za-z]{1,13}-[0-9a-za-za-z]{1,20})/', views.activate, name='activate'),
    path('activate(?p<uidb64>[0-9a-za-z_\-]+)/(?p<token>[0-9a-za-z]{1,13}-[0-9a-za-za-z]{1,20})/', views.activate_hr, name='activate_hr'),
    path('all_applicants/', views.all_applicants, name='all_applicants'),


    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('change_password/',views.change_password,name='change_password')
    
]
