# Generated by Django 5.1.3 on 2024-11-19 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meteora', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='make_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_in',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='make_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_in',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
