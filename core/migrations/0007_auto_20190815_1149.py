# Generated by Django 2.1.5 on 2019-08-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190815_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentwork',
            name='code_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recentwork',
            name='notebook_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]