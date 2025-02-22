# Generated by Django 4.1.3 on 2022-11-25 06:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='single_author',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='', max_length=255, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(default='', max_length=255, validators=[django.core.validators.MinLengthValidator(6)])),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('host', models.CharField(blank=True, default='', max_length=255)),
                ('display_name', models.CharField(blank=True, default='', max_length=255)),
                ('url', models.URLField(blank=True, default='')),
                ('github', models.URLField(blank=True, default='')),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_authors', to='authors.single_author')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_followers', to='authors.single_author')),
            ],
        ),
    ]
