from django.contrib import admin
from .models import user, tag, category, post

# Register your models here.
admin.site.register(user)
admin.site.register(tag)
admin.site.register(category)
admin.site.register(post)