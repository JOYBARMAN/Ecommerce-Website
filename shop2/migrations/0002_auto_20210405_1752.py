# Generated by Django 3.1.1 on 2021-04-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_table',
            name='product_image',
            field=models.ImageField(default='', upload_to='shop2/images'),
        ),
    ]
