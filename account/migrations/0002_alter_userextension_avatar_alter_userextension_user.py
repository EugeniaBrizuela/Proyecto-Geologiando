# Generated by Django 4.0.3 on 2022-04-18 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
