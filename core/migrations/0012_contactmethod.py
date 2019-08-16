# Generated by Django 2.1.5 on 2019-08-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_mooc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Contact method')),
                ('code_url', models.URLField()),
            ],
        ),
    ]
