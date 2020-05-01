# Generated by Django 3.0.3 on 2020-04-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactformmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10),
        ),
    ]
