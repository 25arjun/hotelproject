# Generated by Django 3.0.5 on 2020-04-29 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20200428_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Category'),
        ),
    ]
