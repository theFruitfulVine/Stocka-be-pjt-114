# Generated by Django 3.2.4 on 2021-07-05 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocka_api', '0002_auto_20210705_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stocka_api.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stocka_api.vendor'),
        ),
    ]
