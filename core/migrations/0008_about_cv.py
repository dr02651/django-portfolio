# Generated by Django 2.1.5 on 2019-08-15 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190815_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='cv',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
