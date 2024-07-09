from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .utils.models import slug_and_hash_post_title

# Create your models here.
class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, blank=False, null=False)
    user_fname = models.CharField(max_length=50, blank=False, null=False)
    user_lname = models.CharField(max_length=50, blank=False, null=False)
    user_email = models.EmailField(max_length=254, blank=False, null=False)
    
    def __str__(self):
        return f"{self.user_name} - {self.user_fname} {self.user_lname}"
    
class tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30, blank=False, null=False)
    
    def __str__(self):
        return str(self.tag_name)
    
class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, blank=False, null=False)
    
    def __str__(self):
        return str(self.category_name)
  
POST_STATUS_POSSIBLE_VALUES = [
    "Published",
    "Archived",
    "Deleted"
]

POST_STATUS_CHOICES = [(item, item) for item in POST_STATUS_POSSIBLE_VALUES]

class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    post_title = models.CharField(max_length=150, blank=False, null=False)
    post_content = models.TextField(blank=False, null=False)
    post_published_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=False, null=False)
    post_last_modified = models.DateTimeField(auto_now=True, auto_now_add=False, blank=False, null=False)
    post_slug = models.SlugField(max_length=175, blank=False, null=False)
    post_status = models.CharField(max_length=15, default="Published", blank=False, null=False, choices=POST_STATUS_CHOICES)
    post_description = models.TextField(blank=True, null=True)
    post_featured_img_path = models.CharField(max_length=170, blank=True, null=True)
    post_tags = models.ManyToManyField(tag, blank=True)
    post_categories = models.ManyToManyField(category, blank=True)
    
    def __str__(self):
        return str(self.post_slug)
    
    def save(self, *args, **kwargs):
        new_slug = slug_and_hash_post_title(self.post_title, "tmp")
        self.post_slug = new_slug
        
        super().save(*args, **kwargs)
    
class authentication(models.Model):
    auth_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(user, on_delete=models.CASCADE, null=False, blank=False)
    auth_pass_hash = models.CharField(max_length=12,
                                      blank=False,
                                      null=False,
                                      validators=[
                                          MinLengthValidator(12),
                                          MaxLengthValidator(12),
                                      ],
                                    )
    
    def __str__(self):
        return str(self.user_id)