# Generated by Django 4.0.5 on 2022-09-09 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_companyordeers_sumt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'поставщика', 'verbose_name_plural': 'поставщик'},
        ),
        migrations.AlterField(
            model_name='companyordeers',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyordeers', to='orders.provider', verbose_name='Поставщик'),
        ),
    ]
