# Generated by Django 3.1.3 on 2020-11-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_auto_20201123_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
