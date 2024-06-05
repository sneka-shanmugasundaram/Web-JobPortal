from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Skills(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    name = models.CharField(max_length=200)
    company =models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"


class Location(models.Model):
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.street}"
    


class Company_registration(models.Model):
    emp = (
        ("0-50","0-50"),
        ("100 employees", "100 employees"),
        (" 200 employees", "200 employees"),
        ("more then 500 employees","More Then 500 employees"),
    )
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    company_name =models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    street= models.CharField(max_length=500,null=True)
    city= models.CharField(max_length=500,null=True)
    state= models.CharField(max_length=500,null=True)
    pincode= models.IntegerField(null=True)
    phone_no=models.CharField(max_length=10,null=True)
    type_of_industry= models.CharField(max_length=500,null=True)
    number_of_employee= models.CharField(max_length=500,null=True)
    website= models.CharField(max_length=100,null=True)
    type = models.CharField(max_length=15,null=True)


    def __str__(self):
        return f"{self.user}"
    

class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
    ]
    CHOICE = [
        ('not_ok', 'not_ok'),
        ('ok', 'ok'),
    ]
    ac=[
        ("active","active"),
        ("closed","closed"),
    ]
    image = models.ImageField(upload_to="",null=True,help_text="<br><b>Enter company logo!!<b>")
    company=models.ForeignKey(Company_registration,on_delete=models.CASCADE,null=True)
    c_name= models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)
    expiry=models.DateField(null=True)
    salary = models.CharField(max_length=100,null=True)
    slug = models.SlugField(null=True,max_length=40,unique=True)
    location =models.ForeignKey(Location,on_delete=models.CASCADE)
    author =models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    skills=models.ManyToManyField(Skills)
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)
    status=models.CharField(max_length=20,choices=ac,default="active")
    roll=models.CharField(max_length=50,choices=CHOICE,default="not_ok")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost,self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"


    
class Address(models.Model):
    street=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    country=models.CharField(max_length=200,null=True)
    zip=models.CharField(max_length=200,null=True)
    def __str__(self):
        return f"{self.city}"
    
class Ten_th(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    ten_education = models.CharField(max_length=10,null=True)
    Board = models.CharField(max_length=20,null=True)
    passing_out_year = models.IntegerField(null=True)
    school_medium = models.CharField(max_length=50,null=True)
    total_mark_ten = models.IntegerField(null=True)


class Twelve_th(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    twelve_education = models.CharField(max_length=10,null=True)
    Board = models.CharField(max_length=200,null=True)
    passing_out_year = models.IntegerField(null=True)
    school_medium = models.CharField(max_length=50,null=True)
    total_mark_twelve = models.IntegerField(null=True)
    

class UG(models.Model):
    type =(
        ("FULL TIME","full time"),
        ("PART TIME","part time"),
        ("CORRESPONDANCE/DISTANCE LEARNING","correspondance/distance learning"),
    )
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    ug_education = models.CharField(max_length=100,null=True)
    institude = models.CharField(max_length=200,null=True)
    university = models.CharField(max_length=100,null=True)
    course = models.CharField(max_length=100,null=True)
    specialization = models.CharField(max_length=100,null=True)
    course_type = models.CharField( max_length=200,choices=type,null=True)
    course_duration_from= models.IntegerField(null=True)
    course_duration_to= models.IntegerField(null=True)
    CGPA_ug = models.IntegerField(null=True)

class PG(models.Model):
    type =(
        ("FULL TIME","full time"),
        ("PART TIME","part time"),
        ("CORRESPONDANCE/DISTANCE LEARNING","correspondance/distance learning"),
    )
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    pg_education = models.CharField(max_length=100,null=True)
    institude = models.CharField(max_length=200,null=True)
    university = models.CharField(max_length=100,null=True)
    course = models.CharField(max_length=100,null=True)
    specialization = models.CharField(max_length=100,null=True)
    course_type = models.CharField( max_length=200,choices=type,null=True)
    course_duration_from= models.IntegerField(null=True)
    course_duration_to= models.IntegerField(null=True)
    CGPA_pg = models.IntegerField(null=True)

class J_Skill(models.Model):
    experience=(
        ("0 to 0 Months", "0 to 0 months"),
        ("0 to 6 Months", "0 to 6 months"),
        ("1 to 2 Years", "1 to 2 years"),
        ("more then 2 years","More Then 2 Years"),
    )
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    skill = models.CharField(max_length=200,null=True)
    experience = models.CharField(max_length=200,choices=experience,null=True)

class Certification(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    course_name = models.CharField(max_length=200,null=True)
    certificate = models.FileField(null=True )

class Projects(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    project_title=models.CharField(max_length=200,null=True)
    domain = models.CharField(max_length=200,null=True)
    skills_and_tools = models.CharField(max_length=200,null=True)

class Profile(models.Model):
    exp = (
        ("Fresher","fresher"),
        ("0 to 6 Months", "0 to 6 months"),
        ("1 to 2 Years", "1 to 2 years"),
        ("more then 2 years","More Then 2 Years"),
    )
    image = models.ImageField(upload_to="",null=True,help_text="<br><b>upload your profile picture!!<b>")
    user =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Full_Name = models.CharField(max_length=20)
    DOB = models.DateField(null=True,blank=True)
    email=models.EmailField(null=True)
    phone_number=models.CharField(max_length=10)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    objectives = models.CharField(max_length=200,null=True)
    Resume= models.FileField(null=True)
    Ten_th = models.ForeignKey(Ten_th,on_delete=models.CASCADE,null=True)
    Twelve_th = models.ForeignKey(Twelve_th,on_delete=models.CASCADE,null=True)
    uG = models.ForeignKey(UG,on_delete=models.CASCADE,null=True)
    PG = models.ForeignKey(PG,on_delete=models.CASCADE,blank=True,null=True)
    experience=models.CharField(max_length=50,choices=exp, default="fresher",null=True)
    skill=models.ManyToManyField(J_Skill)
    certification = models.OneToOneField(Certification,on_delete=models.CASCADE,blank=True,null=True)
    projects =models.OneToOneField(Projects,null=True,on_delete=models.CASCADE,blank=True)
    type = models.CharField(max_length=15)
    


    def __str__(self):
        return f"{self.Full_Name}"



def validate_file_extension(value):
    allowed_extensions = ['.doc', '.docx', '.pdf']
    ext = value.name.split('.')[-1]
    if not ext.lower() in allowed_extensions:
        raise ValidationError(_('Invalid file type. Only .doc, .docx, and .pdf files are allowed.'))
        return False
    
    
class JobTitle(models.Model):
    company_name=models.ForeignKey(Company_registration,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    expiry=models.DateField(null=True)
    def __str__(self):
        return f"{self.name}"





class Application(models.Model):
    company = models.CharField(max_length=200, default="")
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    jobtitle = models.ForeignKey(JobTitle,on_delete=models.CASCADE,null=True)
    applicant = models.ForeignKey(Profile,on_delete=models.CASCADE)
    resume = models.FileField(upload_to="download",null=True)
    apply_date = models.DateField(null=True)
    def __str__ (self):
        return f"{self.job}"
    def __str__(self):
        return f"{self.applicant}"