# Generated by Django 3.0.5 on 2020-09-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='salary',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]