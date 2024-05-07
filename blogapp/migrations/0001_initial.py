# Generated by Django 5.0.2 on 2024-03-04 04:40

import blogapp.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='commenttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.CharField(max_length=32)),
                ('comment_time', models.DateTimeField()),
                ('is_delete', models.BooleanField(default=False)),
                ('comment_by', models.CharField(max_length=100)),
                ('cmt', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'commenttable',
            },
        ),
        migrations.CreateModel(
            name='User_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'User_register',
            },
        ),
        migrations.CreateModel(
            name='usertag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagid', models.CharField(max_length=32)),
                ('tag_by', models.CharField(max_length=50)),
                ('tag_to', models.CharField(max_length=50)),
                ('tag_title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'usertag',
            },
        ),
        migrations.CreateModel(
            name='BlogTable',
            fields=[
                ('reference_id', models.CharField(default=blogapp.models.generate_uuid, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('username', models.CharField(max_length=50, null=True)),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(db_column='updated_by', null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'BlogTable',
            },
        ),
    ]
