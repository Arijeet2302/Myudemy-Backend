# Generated by Django 4.2.4 on 2023-12-19 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_cart_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='course_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.courses'),
        ),
    ]
