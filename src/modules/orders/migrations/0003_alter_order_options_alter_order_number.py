# Generated by Django 4.1 on 2022-08-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_change_date_order_changed_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['number']},
        ),
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
