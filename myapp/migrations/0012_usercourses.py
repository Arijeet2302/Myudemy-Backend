# Generated by Django 4.2.4 on 2023-12-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_cart_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=1000)),
                ('cust_name', models.CharField(max_length=50)),
                ('course_name', models.CharField(default='')),
                ('rating', models.FloatField()),
                ('author_name', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='static')),
            ],
        ),
    ]