# Generated by Django 3.0.5 on 2020-05-01 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20200429_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Category'),
        ),
    ]