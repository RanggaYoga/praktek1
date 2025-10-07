from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Warga, Pengaduan

admin.site.register(Warga)
admin.site.register(Pengaduan)