# Generated by Django 5.0.3 on 2024-06-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0004_alter_menuitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='category_description',
            field=models.TextField(default=None),
        ),
    ]
