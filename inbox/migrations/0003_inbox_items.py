# Generated by Django 4.1.2 on 2022-11-25 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_like'),
        ('inbox', '0002_inbox_delete_inboxitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
