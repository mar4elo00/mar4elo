# Generated by Django 4.0.5 on 2022-09-17 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/product'),
        ),
    ]
