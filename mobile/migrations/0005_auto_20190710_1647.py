# Generated by Django 2.2 on 2019-07-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0004_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='gallery'),
        ),
    ]