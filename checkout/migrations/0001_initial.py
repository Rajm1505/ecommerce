# Generated by Django 4.1.3 on 2022-12-06 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Useraddress',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=150)),
                ('phone', models.CharField(default=None, max_length=10)),
                ('pincode', models.CharField(default=None, max_length=6)),
                ('locality', models.CharField(default=None, max_length=100, null=True)),
                ('address', models.CharField(default=None, max_length=255)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('addresstype', models.CharField(choices=[('home', 'Home'), ('work', 'Work')], max_length=30)),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
