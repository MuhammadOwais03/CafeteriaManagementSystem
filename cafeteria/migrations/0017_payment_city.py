# Generated by Django 5.0.3 on 2024-07-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0016_alter_payment_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
