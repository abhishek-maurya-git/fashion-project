# Generated by Django 2.2.5 on 2019-09-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
