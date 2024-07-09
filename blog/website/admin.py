from django.contrib import admin
from .models import user, tag, category, post, authentication

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    readonly_fields = ("post_slug", )

# Register your models here.
admin.site.register(user)
admin.site.register(tag)
admin.site.register(category)
admin.site.register(authentication)