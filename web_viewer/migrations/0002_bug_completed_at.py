# Generated by Django 2.2.4 on 2019-08-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='completed_at',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
