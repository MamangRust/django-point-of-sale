# Generated by Django 5.0 on 2023-12-12 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_cartnumber_payment_cvv_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order',
        ),
    ]