# Generated by Django 5.0.2 on 2024-02-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_remove_sent_logs_suscriptor_sent_logs_count_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='count_sent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='date_sent',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Sent_Logs',
        ),
    ]