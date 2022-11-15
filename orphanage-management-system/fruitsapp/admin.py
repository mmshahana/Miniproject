from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(regmodel)
admin.site.register(orphanage_user)
admin.site.register(orphanagemodel)
admin.site.register(donationmodel)