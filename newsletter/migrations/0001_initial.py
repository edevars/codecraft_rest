# Generated by Django 5.0.2 on 2024-02-15 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('suscribed', models.BooleanField(default=True)),
                ('excluded_categories', models.ManyToManyField(to='newsletter.category')),
            ],
        ),
        migrations.CreateModel(
            name='Sent_Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletter.newsletter')),
                ('suscriptor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletter.suscriptor')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletter.category')),
            ],
        ),
        migrations.AddField(
            model_name='newsletter',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsletter.template'),
        ),
    ]
