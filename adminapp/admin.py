from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import carrers, contact
class contactadmin(admin.ModelAdmin):
    list_display = ['firstname','email','message','time','mobno']
    list_filter = ['time']
class meta:
    model=contact
class carreradmin(admin.ModelAdmin):
    list_display = ['job_title','req_skills','contact_no','update_time','job_location']
    list_filter = ['job_title','update_time','job_location']
class meta:
    model=carrers
    admin.site.register(contact,contactadmin)
    admin.site.register(carrers,carreradmin)