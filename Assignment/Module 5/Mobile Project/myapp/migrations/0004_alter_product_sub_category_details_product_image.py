# Generated by Django 4.2.5 on 2023-10-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_product_sub_category_details_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_sub_category_details',
            name='product_image',
            field=models.FileField(upload_to='product_image/'),
        ),
    ]
