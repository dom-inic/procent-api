# Generated by Django 4.1.7 on 2023-08-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='disccount',
            new_name='discount',
        ),
    ]
