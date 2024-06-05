from datetime import date, timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost,Company_registration
from jobapp import settings
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,update_session_auth_hash
from django.contrib.auth import logout as go


# EMAIL
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import generate_token,generate_token_hr    
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Count
# Create your views here.
job_title=[
    "First_Job",
    "Second_Job",
    "Third_Job"
            ]

job_details=[
    "First_Job_Describtion",
     "Second_Job_Describtion" ,
     "Third_Job_Describtion"
     ]
def home(request):
   context ={}
   return render(request,"app/home.html",context)

def jobs(request):
   if 'quary' in request.GET:
       q = request.GET['quary']
       multiple_q = Q(Q(title__icontains = q) | Q(location__city__icontains = q))
       jobs = JobPost.objects.filter(multiple_q)
   else:
       jobs=JobPost.objects.all()
   context={"jobs":jobs}
   return render(request,"app/jobs.html",context)

def view(request,id):
      
#    try:
#       if id == 0:
#          return redirect(reverse('jobs_home'))  
      user=request.user
    #   print(user)
      job = JobPost.objects.get(id=id)
      #applicant = Profile.objects.get(user=user)
      #apply = Application.objects.filter(applicant=applicant)
    #   data = []
    #   for i in apply:
    #      data.append(i.job.id)
      user=request.user
      com =Company_registration.objects.all()
      print(job.company)
      skill=job.skills.all()
      context={"job":job,"skill":skill,"com":com}
      return render(request,"app/view.html",context)
#    except:
#       return HttpResponseNotFound("Not found")
   
def applyPage(request,id):
    user = request.user
    applicant = Profile.objects.get(user=user)
    sne = JobPost.objects.get(id=id)
    date1 = date.today()
    if request.method == "POST":
            resume = request.FILES['resume']
            Application.objects.create(job=sne, company=sne.company, jobtitle=JobTitle.objects.get(name=sne,company_name=sne.company), applicant=applicant, resume=resume, apply_date=date.today())
            alert=True
            #return render(request, "app/apply.html", {'alert':alert})
            return redirect('jobs')
    return render(request, "app/apply.html", {'sne':sne})
def register(request):
   form = NewUserForm()
   if request.method=="POST":
      form = NewUserForm(request.POST)
      if form.is_valid():
          user = form.save()
          user.is_active = False
          user.save()
          current_site = get_current_site(request)  
          mail_subject = 'Activation link has been sent to your email id'   
          message = render_to_string('email_confirmation.html', {  
                 'user': user,  
                 'domain': current_site.domain,  
                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
               'token':generate_token.make_token(user),  
             })  
          to_email = form.cleaned_data.get('email')  
          email = EmailMessage(  
                         mail_subject, message, to=[to_email]  
             )  
          email.send()   
          return redirect('profile')
      
   context ={"form":form}
   return render(request,'registration/register.html',context)


def activate(request, uidb64, token):  
     User = get_user_model()  
     try:  
         uid = force_str(urlsafe_base64_decode(uidb64))  
         user = User.objects.get(pk=uid)  
     except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
         user = None  
     if user is not None and generate_token.check_token(user, token):  
         user.is_active = True  
         user.save()  
         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
     else:  
         return HttpResponse('Activation link is invalid!') 

def logout(request):
    go(request)
    return redirect('jobs_home')
   

def company_home(request):
   context ={}
   return render(request,'app/company_home.html',context)


def company_signup(request):
    if request.method=="POST":   
        username = request.POST['username']
        #user_instance = User.objects.get(username=username)
        company_name = request.POST['company_name']
        email=request.POST['email']
        Street=request.POST['Street']
        City= request.POST['City']
        State = request.POST['State']
        Pincode = request.POST['Pincode']
        phone = request.POST['phone']
        indus = request.POST['indus']
        emp = request.POST['emp']
        Website = request.POST['Website']
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username.")
            return redirect('r_company')
        if company_name =="":
            messages.error(request,"enter company name")
            return redirect('r_company')
        if Street == "":
            messages.error(request,"enter street name")
            return redirect('r_company')
        if City == "":
            messages.error(request,"enter city name")   
            return redirect('r_company')
        if State == "":
            messages.error(request,"enter state name")
            return redirect('r_company')
        if Website == "":
            messages.error(request,"enter website name")
            return redirect('r_company')
        
        if emp == "":
            messages.error(request,"enter number of employees")
            return redirect('r_company')
        
        if indus == "":
            messages.error(request,"enter type of industry")
            return redirect('r_company')
        if len(phone)!=10:
            messages.error(request,"please enter valid phone number!")
            return redirect('r_company')
        if len(Pincode)!=6:
            messages.error(request,"enter valid pincode!")
            return redirect('r_company')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('r_company')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('r_company')
        
        user = User.objects.create_user(username=username, email=email,password=company_name)
        company = Company_registration.objects.create(user=user,company_name=company_name,email=email,street=Street,
        city=City,state=State,pincode=Pincode,phone_no=phone,type_of_industry=indus,number_of_employee=emp,website=Website,type="company")
        user.save()
        user.is_active = False
        company.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to TECH- Django Login!!"
        message = "Hello " + user.username + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address.\n Username   :"+ user.username +"\n Password   :"+ company.company_name +"\n\nThanking You\n sneka"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation_hr.html',{
            
            'name': user.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [user.email],
        )
        email.fail_silently = True
        email.send()
        
        
      
        return render(request, 'app/l_company.html')
    return render(request, 'app/r_company.html')


def company_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
 
        if user is not None:
            user1 = Company_registration.objects.get(user=user)
            if user1.type == "company":
                login(request, user)
                return redirect('company_home')
        else:
            alert = True
            return render(request, "app/l_company.html", {"alert":alert})
    return render(request, "app/l_company.html")



def postform(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        # user = request.user
        # print(user)
        # company = Company_registration.objects.get(user=user)
        # print(company)
        # j = JobPost.objects.create(company=company)
        # j.save()
        if form.is_valid():
            form.save()
            return redirect('saveform')
        
    context={'form':form}
    return render(request,'app/post.html',context)
def updateform(request,id):
    if request.user.is_authenticated:
        c_job=JobPost.objects.get(id=id)
        form = PostForm(request.POST or None,instance=c_job)
        if form.is_valid():
            form.save()
            return redirect('all_applicants')
        return render(request,'app/update.html',{'form':form})
    else:
        return redirect('jobs_home')



def closeform(request,id):
    if request.user.is_authenticated:
       u_job=JobPost.objects.get(id=id)
       form=close(request.POST or None,instance=u_job)
       if form.is_valid():
          form.save()
          return redirect('all_applicants')
       return render(request,'app/close.html',{'form':form})
    else:
        return redirect('jobs_home')
    


def infoform(request,id):
    if request.user.is_authenticated:
       u_job=JobPost.objects.get(id=id)
       return render(request,'app/abs.html',{'u_job':u_job})



def saveform(request):
    form=SaveForm()
    if request.method=='POST':
        form=SaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_home')
        
    context={'form':form}
    return render(request,'app/saveform.html',context)


def locationform(request):
    form=LocationForm()
    if request.method=='POST':
        form=LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
        
    context={'form':form}
    return render(request,'app/location.html',context)



def authorform(request):
    form=AuthorForm()
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
        
    context={'form':form}
    return render(request,'app/author.html',context)

   

def skillform(request):
    form=SkillForm()
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
        
    context={'form':form}
    return render(request,'app/skill.html',context)

   
def profileform(request):
    forms = ProfileForm()
    if request.method =='POST':
        forms = ProfileForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('jobs')
    context ={'forms':forms}
    return render(request,'app/profile.html',context)

def upform(request,id):
    if request.user.is_authenticated:
        c_job=Profile.objects.get(id=id)
        form = ProfileForm(request.POST or None,instance=c_job)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        return render(request,'app/upform.html',{'form':form})
    else:
        return redirect('jobs_home')


def tenthform(request):
    form=tenth()
    if request.method=='POST':
        form=tenth(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        
    context={'form':form}
    return render(request,'app/tenth.html',context)

def profile_view(request,id):
#    try:
#     if id == 0:
#          return redirect('jobs_home')
    user=request.user
    profile=Profile.objects.get(id=id)
    # ten =Ten_th.objects.get(user=user)
    #Twelve =Twelve_th.objects.get(user=user)
    context ={"profile":profile}
    return render(request,"app/p1.html",context)
#    except:
#        return HttpResponseNotFound("not found")
def activate_hr(request, uidb64, token):   
     try:  
         uid = force_str(urlsafe_base64_decode(uidb64))  
         HR = Company_registration.objects.get(pk=uid)  
     except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
         HR = None  
     if HR is not None and generate_token.check_token(HR, token):  
         HR.is_active = True  
         HR.save()  
         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
     else:  
         return HttpResponse('Activation link is invalid!') 

   
   
def all_applicants(request):
    user=request.user
    #job = JobPost.objects.all()
    today=date.today()
    # # for i in jobs:
    # #     print(i.title)
    company = Company_registration.objects.get(user=user)
    application = Application.objects.filter(company=company)
    # return render(request, "app/all_applicants.html", {'application':application,"jobs":jobs})
    all = JobTitle.objects.annotate(total=Count('application')).filter(company_name=company)
    job = JobPost.objects.all()
    return render(request, "app/all_applicants.html", {'all':all,'application':application,"job":job,"today":today})


def applicants(request,id):
    user=request.user
    jobs = JobPost.objects.filter(id=id) 
    app=JobTitle.objects.all()
    company = Company_registration.objects.get(user=user)
    application = Application.objects.filter(job_id=id)
    print(type(jobs))
    # name=[]
    for i in application:
       if i.job == jobs:
           print(i.job)

    return render(request, "app/applicants.html", {'application':application,"app":app,"jobs":jobs})




def change_password(request):
    if request.method=='POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return redirect('company_home')
        else:
            fm=PasswordChangeForm(user=request.user)
            return render(request,'change_password.html',{'fm':fm})

        
    else:
        fm=PasswordChangeForm(user=request.user)
        return render(request,'change_password.html',{'fm':fm})

