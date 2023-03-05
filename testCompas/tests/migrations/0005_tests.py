# Generated by Django 4.1.1 on 2023-01-20 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_alter_tasks_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer1', models.TextField()),
                ('answer2', models.TextField()),
                ('answer3', models.TextField()),
                ('answer4', models.TextField()),
                ('correct', models.TextField()),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.units')),
            ],
        ),
    ]
