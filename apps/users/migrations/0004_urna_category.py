# Generated by Django 4.0.5 on 2022-09-17 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_brend_appointment'),
        ('users', '0003_urna_summ_alter_urna_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='urna',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='product.category', verbose_name='Категория'),
        ),
    ]
