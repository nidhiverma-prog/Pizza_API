# Generated by Django 3.1.4 on 2020-12-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(default=None, max_length=50)),
                ('pizza_size', models.CharField(default=None, max_length=50)),
                ('toppings', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]