# Generated by Django 4.2.4 on 2023-08-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(default='', upload_to='static'),
        ),
    ]
