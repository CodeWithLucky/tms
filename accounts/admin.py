from django.contrib import admin
from . models import CustomUser, Work
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Work)