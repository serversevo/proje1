# Generated by Django 3.0.3 on 2020-05-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]
