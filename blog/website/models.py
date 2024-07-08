from django.db import models

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
    
class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    post_title = models.CharField(max_length=150, blank=False, null=False)
    post_content = models.TextField(blank=False, null=False)
    post_published_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=False, null=False)
    post_last_modified = models.DateTimeField(auto_now=True, auto_now_add=False, blank=False, null=False)
    post_slug = models.SlugField(max_length=175, blank=False, null=False)
    post_status = models.CharField(max_length=15, default="Published", blank=False, null=False)
    post_description = models.TextField(blank=True, null=True)
    post_featured_img_path = models.CharField(max_length=170, blank=True, null=True)
    post_tags = models.ManyToManyField(tag)
    post_categories = models.ManyToManyField(category)