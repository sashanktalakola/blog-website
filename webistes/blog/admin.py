from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.POST)
admin.site.register(models.COMMENT)
admin.site.register(models.TAG)
admin.site.register(models.USER)