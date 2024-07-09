from django.contrib import admin
from .models import user, tag, category, post, authentication

# Register your models here.
admin.site.register(user)
admin.site.register(tag)
admin.site.register(category)
admin.site.register(post)
admin.site.register(authentication)