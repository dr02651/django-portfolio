# Generated by Django 2.1.5 on 2019-08-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recentwork_photo_credit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recentwork',
            old_name='url',
            new_name='code_url',
        ),
        migrations.RemoveField(
            model_name='recentwork',
            name='file_type',
        ),
        migrations.AddField(
            model_name='recentwork',
            name='code_status',
            field=models.CharField(choices=[('enabled', 'enabled'), ('disabled', 'disabled')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recentwork',
            name='notebook_status',
            field=models.CharField(choices=[('enabled', 'enabled'), ('disabled', 'disabled')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recentwork',
            name='notebook_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
