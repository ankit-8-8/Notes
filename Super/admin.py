from django.contrib import admin
from .models import *
# Register your models here.


class postAdmin(admin.ModelAdmin):
    list_display = ('pheading','pcreated_by','pdate','ptime')
admin.site.register(post,postAdmin)

class tbl_registerAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','username')
admin.site.register(tbl_register,tbl_registerAdmin)

class tbl_superAdmin(admin.ModelAdmin):
    list_display=('name','email','password','mobile')
admin.site.register(tbl_super,tbl_superAdmin)