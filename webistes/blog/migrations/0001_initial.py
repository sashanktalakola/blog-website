# Generated by Django 5.0.3 on 2024-03-22 15:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAG',
            fields=[
                ('TAG_ID', models.AutoField(primary_key=True, serialize=False)),
                ('TAG_NAME', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('USER_ID', models.AutoField(primary_key=True, serialize=False)),
                ('USER_FNAME', models.CharField(max_length=30)),
                ('USER_LNAME', models.CharField(max_length=30)),
                ('USER_EMAIL', models.EmailField(max_length=50)),
                ('USER_AUTH_PASSWORD', models.CharField(max_length=30)),
                ('AUTH_TOKEN', models.CharField(max_length=72)),
            ],
        ),
        migrations.CreateModel(
            name='POST',
            fields=[
                ('POST_ID', models.SlugField(primary_key=True, serialize=False)),
                ('POST_TITLE', models.CharField(max_length=50)),
                ('POST_OVERVIEW', models.TextField(max_length=100)),
                ('POST_CONTENT', models.TextField()),
                ('POST_DATETIME', models.DateTimeField(auto_now=True)),
                ('USER_ID', models.ForeignKey(db_column='USER_ID', on_delete=django.db.models.deletion.CASCADE, to='blog.user')),
            ],
        ),
        migrations.CreateModel(
            name='COMMENT',
            fields=[
                ('COMMENT_ID', models.AutoField(primary_key=True, serialize=False)),
                ('COMMENT_CONTENT', models.TextField(max_length=200)),
                ('COMMENT_LIKES', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('COMMENT_DISLIKES', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('COMMENT_DATETIME', models.DateTimeField(auto_now=True)),
                ('COMMENT_REPLY', models.ForeignKey(blank=True, db_column='REPLY_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comment')),
                ('POST_ID', models.ForeignKey(db_column='POST_ID', on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('USER_ID', models.ForeignKey(db_column='USER_ID', on_delete=django.db.models.deletion.CASCADE, to='blog.user')),
            ],
        ),
    ]
