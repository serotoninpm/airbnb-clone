# Generated by Django 2.2.5 on 2022-09-04 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20220710_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.OneToOneField(on_delete=80, related_name='lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
