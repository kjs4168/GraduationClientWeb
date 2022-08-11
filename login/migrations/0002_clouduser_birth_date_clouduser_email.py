# Generated by Django 4.1 on 2022-08-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clouduser',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clouduser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]