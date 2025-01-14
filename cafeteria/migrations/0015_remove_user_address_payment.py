# Generated by Django 5.0.3 on 2024-07-02 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0014_order_order_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
                ('payment_type', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafeteria.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafeteria.user')),
            ],
        ),
    ]
