# Generated by Django 4.0.5 on 2022-09-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_passport_data_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passport_data',
            old_name='employee',
            new_name='employeer',
        ),
        migrations.AlterField(
            model_name='passport_data',
            name='date_end',
            field=models.DateField(max_length=255, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='passport_data',
            name='date_start',
            field=models.DateField(max_length=255, verbose_name='Дата получения'),
        ),
    ]