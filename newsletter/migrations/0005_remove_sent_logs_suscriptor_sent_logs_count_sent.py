# Generated by Django 5.0.2 on 2024-02-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_rename_atached_file_template_attached_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sent_logs',
            name='suscriptor',
        ),
        migrations.AddField(
            model_name='sent_logs',
            name='count_sent',
            field=models.IntegerField(default=0),
        ),
    ]
