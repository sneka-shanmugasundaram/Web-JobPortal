from django.contrib import admin
from app.models import  JobPost,Profile,Company_registration,Application


class JobAdmin(admin.ModelAdmin):
    list_display= ('title','c_name')
    list_filter =('date','salary','expiry')
    search_fields= ('title','description')
    search_help_text="write your text"
    #fields = ('title','description','expiry')
    #exclude =('title',)
    fieldsets =(
        ('Basic information',{
            'fields':('title','description')
        }),
        ('More information',{
            'classes':('collapse','wide'),
            'fields':(('expiry','salary'),'slug')
        }),
    )    
#Register your models here.
admin.site.register(JobPost)
admin.site.register(Profile)
admin.site.register(Company_registration)
admin.site.register(Application)


# Register your models here.
