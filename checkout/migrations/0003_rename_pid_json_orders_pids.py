# Generated by Django 4.1.3 on 2022-12-16 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='pid_json',
            new_name='pids',
        ),
    ]
