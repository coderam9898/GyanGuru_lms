# Generated by Django 3.2 on 2022-09-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20220901_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]
