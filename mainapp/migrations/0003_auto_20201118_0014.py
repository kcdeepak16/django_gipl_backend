# Generated by Django 3.0.3 on 2020-11-17 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20201117_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sub_categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.sub_categories'),
        ),
        migrations.AlterField(
            model_name='sub_categories',
            name='pcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.categories'),
        ),
    ]
