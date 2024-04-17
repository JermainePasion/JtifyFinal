# Generated by Django 5.0.1 on 2024-03-19 09:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_artistregister_verification_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistregister',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
