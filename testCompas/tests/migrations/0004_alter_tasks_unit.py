# Generated by Django 4.1.1 on 2023-01-15 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_alter_tasks_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.units'),
        ),
    ]
