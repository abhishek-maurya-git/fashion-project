# Generated by Django 2.2.5 on 2019-10-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191005_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='favorate',
            field=models.BooleanField(default=False),
        ),
    ]