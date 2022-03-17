# Generated by Django 4.0.3 on 2022-03-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('elemento_realizado', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('texto', models.TextField(max_length=120)),
            ],
        ),
    ]
