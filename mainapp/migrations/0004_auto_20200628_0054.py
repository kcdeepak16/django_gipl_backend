# Generated by Django 3.0.3 on 2020-06-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200628_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query',
            field=models.TextField(max_length=1000),
        ),
    ]
