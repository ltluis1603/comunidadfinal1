# Generated by Django 3.0.4 on 2020-06-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20200624_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='project',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='project',
            name='mercado',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Mercado Libre'),
        ),
        migrations.AddField(
            model_name='project',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Twitter'),
        ),
    ]