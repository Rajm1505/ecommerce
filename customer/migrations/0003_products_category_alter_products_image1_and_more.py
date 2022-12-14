# Generated by Django 4.1.3 on 2022-11-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('accessories', 'Accessories'), ('clothing', 'Clothing'), ('healthcare', 'Healthcare')], default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='products',
            name='image1',
            field=models.ImageField(default=None, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(default=None, upload_to='products'),
        ),
    ]
