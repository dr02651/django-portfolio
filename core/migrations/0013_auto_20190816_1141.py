# Generated by Django 2.1.5 on 2019-08-16 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_contactmethod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmethod',
            old_name='code_url',
            new_name='url',
        ),
    ]