# Generated by Django 4.0.5 on 2022-09-09 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.CharField(max_length=255, null=True, unique=True, verbose_name='name 1')),
                ('test2', models.CharField(blank=True, max_length=255, null=True, verbose_name='name 2')),
            ],
            options={
                'verbose_name': 'Test_Name',
                'verbose_name_plural': 'Test_Name',
            },
        ),
    ]
