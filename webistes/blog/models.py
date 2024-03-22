from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class USER(models.Model):
    USER_ID = models.AutoField(primary_key=True)
    USER_FNAME = models.CharField(max_length=30)
    USER_LNAME = models.CharField(max_length=30)
    USER_EMAIL = models.EmailField(max_length=50)
    USER_AUTH_PASSWORD = models.CharField(max_length=30)
    AUTH_TOKEN = models.CharField(max_length=72)

    def __str__(self):
        return f"{self.USER_FNAME} {self.USER_LNAME}"

class TAG(models.Model):
    TAG_ID = models.AutoField(primary_key=True)
    TAG_NAME = models.CharField(max_length=20)

    def __str__(self):
        return self.TAG_NAME

class POST(models.Model):
    POST_ID = models.SlugField(primary_key=True)
    POST_TITLE = models.CharField(max_length=50)
    POST_OVERVIEW = models.TextField(max_length=100)
    POST_CONTENT = models.TextField()
    POST_DATETIME = models.DateTimeField(auto_now=True)
    USER_ID = models.ForeignKey(USER, on_delete=models.CASCADE, db_column="USER_ID")

    def __str__(self):
        reutrn 

class COMMENT(models.Model):
    COMMENT_ID = models.AutoField(primary_key=True)
    POST_ID = models.ForeignKey(POST, on_delete=models.CASCADE, db_column="POST_ID")
    COMMENT_CONTENT = models.TextField(max_length=200)
    USER_ID = models.ForeignKey(USER, on_delete=models.CASCADE, db_column="USER_ID")
    COMMENT_LIKES = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    COMMENT_DISLIKES = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    COMMENT_REPLY = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, db_column="REPLY_ID")
    COMMENT_DATETIME = models.DateTimeField(auto_now=True)